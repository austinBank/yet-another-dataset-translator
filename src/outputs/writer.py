from pathlib import Path
from typing import Any, List, Dict

from translator.utils import save_json_file

def write_output(items: List[Dict[str, Any]], output_path: Path) -> None:
    """
    Write the translated dataset items to the given JSON file.
    """
    save_json_file(output_path, items)