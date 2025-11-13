import json
import logging
from pathlib import Path
from typing import Any, Dict

logger = logging.getLogger(__name__)

def load_json_file(path: Path) -> Any:
    """
    Load JSON from the given path and return the parsed data.
    """
    logger.debug("Loading JSON file from %s", path)
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def save_json_file(path: Path, data: Any) -> None:
    """
    Save data as pretty-printed JSON to the given path.
    """
    logger.debug("Saving JSON file to %s", path)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def ensure_parent_dir(path: Path) -> None:
    """
    Ensure that the parent directory for a path exists.
    """
    parent = path.parent
    if not parent.exists():
        logger.debug("Creating directories for %s", parent)
        parent.mkdir(parents=True, exist_ok=True)