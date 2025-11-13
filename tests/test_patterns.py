import sys
from pathlib import Path

# Ensure src/ is on the Python path
ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from translator.field_selector import select_fields  # type: ignore

def test_select_fields_with_patterns():
    item = {
        "id": 1,
        "text": "Hallo Welt",
        "description": "German example",
        "displayName": "Example",
        "meta_field": "value"
    }
    patterns = ["*text", "*description", "?isplayName", "*_field"]

    selected = select_fields(item, patterns)
    assert "text" in selected
    assert "description" in selected
    assert "displayName" in selected
    assert "meta_field" in selected
    # ID should not match any of the patterns above
    assert "id" not in selected

def test_select_fields_without_patterns_returns_all_keys():
    item = {"a": 1, "b": 2}
    selected = select_fields(item, [])
    assert set(selected) == {"a", "b"}