import json
from json import JSONDecodeError

from pathlib import Path

class ConfigError(Exception):
    pass

required_keys = {"base_path", "categories", "log_config"}

required_folders = {"image","video","other","docs"}
def config_loader(config_path :str = "config/config.json") -> dict :
    config_path = Path(config_path)
    if not config_path.is_file():
        raise ConfigError("config file not found")

    try:
        with open(config_path,'r') as config_file:
            config = json.load(config_file)

    except JSONDecodeError:
         raise ConfigError("config file format is incorrect")

    missing_keys = required_keys - config.keys()
    if missing_keys:
        raise ConfigError(f"Missing required keys: {missing_keys}")

    categories = config["categories"]
    if not isinstance(categories, dict) or not categories:
        raise ConfigError("Categories must be a non-empty dictionary")

    for category, data in categories.items():
        if "folder" not in data or "extension" not in data:
            raise ConfigError(f"Category '{category}' is invalid")

    base_path = Path(config["base_path"])
    if not base_path.exists():
        raise ConfigError("base path not found")

    return config



