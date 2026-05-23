"""Read, update, validate, and save a JSON config file."""

import json
import sys
from pathlib import Path


CONFIG_PATH = Path("config.json")
ALLOWED_THEMES = {"light", "dark"}
ALLOWED_LANGUAGES = {"en", "zh-TW", "zh-CN"}


def load_config(path=CONFIG_PATH):
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")
    with path.open(encoding="utf-8") as file:
        return json.load(file)


def validate_setting(key, value):
    if key == "theme" and value not in ALLOWED_THEMES:
        raise ValueError("theme must be light or dark")
    if key == "language" and value not in ALLOWED_LANGUAGES:
        raise ValueError("language must be en, zh-TW, or zh-CN")
    if key == "font_size":
        try:
            value = int(value)
        except ValueError as exc:
            raise ValueError("font_size must be a number") from exc
        if not 8 <= value <= 32:
            raise ValueError("font_size must be between 8 and 32")
    return value


def update_config(config, key, value):
    if key not in config:
        raise KeyError(f"Unknown setting: {key}")
    config[key] = validate_setting(key, value)
    return config


def save_config(config, path=CONFIG_PATH):
    with path.open("w", encoding="utf-8") as file:
        json.dump(config, file, indent=2, ensure_ascii=False)
        file.write("\n")


def ask_for_update(config):
    print("Current settings:")
    print(json.dumps(config, indent=2, ensure_ascii=False))
    key = input("Setting to change: ").strip()
    value = input("New value: ").strip()
    return key, value


def main():
    try:
        config = load_config()
        if len(sys.argv) == 3:
            key, value = sys.argv[1], sys.argv[2]
        else:
            key, value = ask_for_update(config)
        updated = update_config(config, key, value)
        save_config(updated)
        print("Updated config.json:")
        print(json.dumps(updated, indent=2, ensure_ascii=False))
    except (FileNotFoundError, json.JSONDecodeError, KeyError, ValueError) as exc:
        print(f"Error: {exc}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
