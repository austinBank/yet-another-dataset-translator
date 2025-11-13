import logging
from typing import Any, Dict, Iterable, List, Optional

from .field_selector import select_fields
from .language_detector import LanguageDetector

logger = logging.getLogger(__name__)

try:
    # Optional: real Google Cloud Translate support.
    from google.cloud import translate_v2 as translate  # type: ignore

    _GOOGLE_TRANSLATE_AVAILABLE = True
except Exception:  # pragma: no cover - import guard
    translate = None
    _GOOGLE_TRANSLATE_AVAILABLE = False

class TranslatorEngine:
    """
    Core translation engine which:
    - Selects fields using glob patterns.
    - Optionally performs language detection.
    - Translates only non-target-language fields.
    - Preserves originals with a configurable prefix.
    - Marks items with a translation status field.
    """

    def __init__(
        self,
        api_key: str,
        target_language: str,
        detector: Optional[LanguageDetector],
        field_patterns: Iterable[str],
        marker_field: str = "wasTranslated",
        original_prefix: str = "original_",
        mock_mode: bool = False,
    ) -> None:
        self.api_key = api_key or ""
        self.target_language = target_language
        self.detector = detector
        self.field_patterns = list(field_patterns or [])
        self.marker_field = marker_field
        self.original_prefix = original_prefix
        self.mock_mode = mock_mode

        self._client = None
        if not self.mock_mode and _GOOGLE_TRANSLATE_AVAILABLE and self.api_key:
            # translate.Client uses application default credentials; we keep api_key
            # primarily for configuration consistency.
            self._client = translate.Client()  # pragma: no cover

    def _should_translate_text(self, text: Any) -> bool:
        if text is None:
            return False
        text_str = str(text)
        if not text_str.strip():
            return False
        if self.detector is None:
            return True
        # If threshold <= 0, detector.is_same_language() always False -> always translate.
        return not self.detector.is_same_language(text_str)

    def translate_text(self, text: str) -> str:
        """
        Translate a single text string. Falls back to mock behavior if:
        - mock_mode is enabled, or
        - there is no API key, or
        - Google Cloud Translate library is unavailable.
        """
        text = text or ""
        if (
            self.mock_mode
            or not self.api_key
            or not _GOOGLE_TRANSLATE_AVAILABLE
            or self._client is None
        ):
            # Lightweight mock translation useful for testing and cost-free runs.
            return f"[{self.target_language}] {text}"

        try:  # pragma: no cover - external dependency
            result = self._client.translate(
                text,
                target_language=self.target_language,
            )
            translated = result.get("translatedText", text)
            return translated
        except Exception as exc:  # pragma: no cover - defensive
            logger.warning("Falling back to mock translation due to error: %s", exc)
            return f"[{self.target_language}] {text}"

    def translate_item(self, item: Dict[str, Any]) -> Dict[str, Any]:
        """
        Translate a single item (dictionary) according to configuration.

        - Only fields matching field_patterns are considered.
        - If language detection says "already in target language", the field is skipped.
        - If a field is translated, the original value is stored under:
          f"{original_prefix}{field_name}" (if original_prefix is non-empty).
        - marker_field is set to True if at least one field was translated,
          otherwise False.
        """
        out: Dict[str, Any] = dict(item)
        fields_to_consider = select_fields(item, self.field_patterns)
        translated_any = False

        for field in fields_to_consider:
            original_value = item.get(field)
            if not self._should_translate_text(original_value):
                continue

            translated_text = self.translate_text(str(original_value))
            out[field] = translated_text
            if self.original_prefix:
                original_field_name = f"{self.original_prefix}{field}"
                out[original_field_name] = original_value
            translated_any = True

        if self.marker_field:
            out[self.marker_field] = translated_any

        return out

    def translate_dataset(self, items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Translate a list of items.
        """
        result: List[Dict[str, Any]] = []
        for idx, item in enumerate(items):
            logger.debug("Translating item %d", idx)
            result.append(self.translate_item(item))
        return result