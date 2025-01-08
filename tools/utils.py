import yaml
import os


def load_config(config_path = "config/user_config.yml"):
    if os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)
    else:
        raise FileNotFoundError(f"Файл конфига '{config_path}' не найден.")

def save_config(config):
    config_path = "config/user_config.yml"
    with open(config_path, "w") as file:
        yaml.dump(config, file)


def load_language(lang_path):
    if os.path.exists(lang_path):
        with open(lang_path, "r") as file:
            return yaml.safe_load(file)
    return {}


def setup_logging(log_file):
    import logging
    logging.basicConfig(
        filename=log_file,
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )