from fnmatch import fnmatch
from typing import Dict, Iterable, List, Any

def select_fields(item: Dict[str, Any], patterns: Iterable[str]) -> List[str]:
    """
    Select field names from `item` that match any of the glob-style patterns.

    If no patterns are provided, all keys are selected.
    """
    keys = list(item.keys())
    patterns = list(patterns or [])

    if not patterns:
        return keys

    selected: List[str] = []
    for key in keys:
        for pattern in patterns:
            if fnmatch(key, pattern):
                selected.append(key)
                break
    return selected