import argparse
import logging
import os
from pathlib import Path
from typing import Any, Dict, List

from translator.language_detector import LanguageDetector
from translator.translator_engine import TranslatorEngine
from translator.utils import load_json_file, ensure_parent_dir
from outputs.writer import write_output

def load_config(config_path: Path) -> Dict[str, Any]:
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")
    config = load_json_file(config_path)

    # Allow overrides via environment variables
    api_key = os.getenv("GOOGLE_TRANSLATE_API_KEY") or config.get("api_key") or ""
    config["api_key"] = api_key

    return config

def build_engine_from_config(config: Dict[str, Any]) -> TranslatorEngine:
    target_language = config.get("target_language", "en")
    threshold = float(config.get("detect_language_threshold", 0.7))
    detector = LanguageDetector(target_language=target_language, threshold=threshold)

    field_patterns = config.get("field_patterns_to_translate", ["*"])
    marker_field = config.get("translation_marker_field", "wasTranslated")
    original_prefix = config.get("original_value_field_prefix", "original_")
    mock_mode = bool(config.get("mock_mode", False))

    engine = TranslatorEngine(
        api_key=config.get("api_key", ""),
        target_language=target_language,
        detector=detector,
        field_patterns=field_patterns,
        marker_field=marker_field,
        original_prefix=original_prefix,
        mock_mode=mock_mode,
    )
    return engine

def load_input_items(input_path: Path) -> List[Dict[str, Any]]:
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    data = load_json_file(input_path)
    if not isinstance(data, list):
        raise ValueError("Input data must be a JSON array of objects.")
    return data

def configure_logging(verbose: bool = False) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Yet Another Dataset Translator - translate JSON datasets with smart language detection."
    )
    parser.add_argument(
        "--input",
        "-i",
        default="data/input.sample.json",
        help="Path to input JSON file (array of objects). Default: data/input.sample.json",
    )
    parser.add_argument(
        "--output",
        "-o",
        default="data/output.example.json",
        help="Path to output JSON file. Default: data/output.example.json",
    )
    parser.add_argument(
        "--config",
        "-c",
        default="src/config/settings.json",
        help="Path to config JSON file. Default: src/config/settings.json",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose logging.",
    )
    return parser.parse_args()

def main() -> None:
    args = parse_args()
    configure_logging(args.verbose)

    logger = logging.getLogger("main")

    input_path = Path(args.input)
    output_path = Path(args.output)
    config_path = Path(args.config)

    logger.info("Loading configuration from %s", config_path)
    config = load_config(config_path)

    logger.info("Initializing translation engine")
    engine = build_engine_from_config(config)

    logger.info("Loading input dataset from %s", input_path)
    items = load_input_items(input_path)

    logger.info("Translating %d items (mock_mode=%s)", len(items), engine.mock_mode)
    translated_items = engine.translate_dataset(items)

    ensure_parent_dir(output_path)
    logger.info("Writing translated items to %s", output_path)
    write_output(translated_items, output_path)

    logger.info("Done. Translated items written to %s", output_path)

if __name__ == "__main__":
    main()