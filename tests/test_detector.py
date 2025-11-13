import sys
from pathlib import Path

import pytest

# Ensure src/ is on the Python path
ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from translator.language_detector import LanguageDetector  # type: ignore

@pytest.mark.parametrize(
    "text,expected_lang",
    [
      ("Hello, how are you?", "en"),
      ("Bonjour tout le monde", "fr"),
      ("Guten Tag", "de"),
    ],
)
def test_detect_language_basic(text, expected_lang):
    detector = LanguageDetector(target_language="en", threshold=0.7)
    lang, prob = detector.detect_language(text)
    assert isinstance(lang, str)
    assert isinstance(prob, float)
    assert 0.0 <= prob <= 1.0
    assert len(lang) == 2

def test_is_same_language_true_for_english():
    detector = LanguageDetector(target_language="en", threshold=0.5)
    assert detector.is_same_language("This is an English sentence.") is True

def test_is_same_language_false_for_non_english():
    detector = LanguageDetector(target_language="en", threshold=0.5)
    assert detector.is_same_language("Das ist ein deutscher Satz.") is False

def test_detection_disabled_when_threshold_zero():
    detector = LanguageDetector(target_language="en", threshold=0.0)
    # With threshold 0, is_same_language always returns False -> detection disabled
    assert detector.is_same_language("This is an English sentence.") is False