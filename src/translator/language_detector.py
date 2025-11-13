from typing import Tuple

from langdetect import DetectorFactory, detect_langs

DetectorFactory.seed = 0

class LanguageDetector:
    """
    Thin wrapper around langdetect providing a confidence threshold and
    a simple "same language as target" helper.

    If threshold <= 0, language detection is considered disabled and
    all texts are treated as not being in the target language.
    """

    def __init__(self, target_language: str = "en", threshold: float = 0.7) -> None:
        self.target_language = target_language
        self.threshold = float(threshold)

    def detect_language(self, text: str) -> Tuple[str, float]:
        """
        Detect language and return (language_code, probability).
        """
        cleaned = (text or "").strip()
        if not cleaned:
            return self.target_language, 1.0

        try:
            candidates = detect_langs(cleaned)
        except Exception:
            # If detection fails, fall back to target language with low confidence.
            return self.target_language, 0.0

        if not candidates:
            return self.target_language, 0.0

        top = candidates[0]
        return top.lang, float(getattr(top, "prob", 0.0))

    def is_same_language(self, text: str) -> bool:
        """
        Returns True if `text` is in the target language with confidence
        >= threshold. If threshold <= 0, returns False (detection disabled).
        """
        if self.threshold <= 0:
            return False

        lang, prob = self.detect_language(text)
        return lang == self.target_language and prob >= self.threshold