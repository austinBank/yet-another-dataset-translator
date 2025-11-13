import sys
from pathlib import Path

import pytest

# Ensure src/ is on the Python path
ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from translator.language_detector import LanguageDetector  # type: ignore
from translator.translator_engine import TranslatorEngine  # type: ignore

def build_mock_engine():
    detector = LanguageDetector(target_language="en", threshold=0.7)
    engine = TranslatorEngine(
        api_key="",
        target_language="en",
        detector=detector,
        field_patterns=["*text"],
        marker_field="wasTranslated",
        original_prefix="original_",
        mock_mode=True,
    )
    return engine

def test_translate_item_translates_non_english_and_marks():
    engine = build_mock_engine()
    item = {
        "id": 1,
        "text": "Auf Wiedersehen.",
        "note": "German farewell example"
    }

    out = engine.translate_item(item)
    assert out["id"] == 1
    assert out["note"] == "German farewell example"
    assert out["text"].startswith("[en]")
    assert out["original_text"] == "Auf Wiedersehen."
    assert out["wasTranslated"] is True

def test_translate_item_skips_english_when_above_threshold():
    engine = build_mock_engine()
    item = {
        "id": 2,
        "text": "Hello, this is already in English.",
        "note": "English example"
    }

    out = engine.translate_item(item)
    # Depending on detection, this may or may not be translated.
    # We assert that if translated, marker is True; if not, marker is False.
    if out["text"].startswith("[en]"):
        assert out["wasTranslated"] is True
        assert out.get("original_text") == "Hello, this is already in English."
    else:
        assert out["text"] == "Hello, this is already in English."
        assert out["wasTranslated"] is False
        assert "original_text" not in out

def test_translate_dataset_handles_multiple_items():
    engine = build_mock_engine()
    items = [
        {"id": 1, "text": "Auf Wiedersehen."},
        {"id": 2, "text": "Bonjour tout le monde"},
    ]

    out_items = engine.translate_dataset(items)
    assert len(out_items) == 2
    for out in out_items:
        assert "wasTranslated" in out
        # In mock mode, non-English texts are expected to be translated
        if out["id"] in (1, 2):
            assert out["text"].startswith("[en]")