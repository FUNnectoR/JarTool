import yaml
import os

class UserSettings:
    @staticmethod
    def load_user_settings():
        settings_file = 'config/user_settings.yml'
        if os.path.exists(settings_file):
            with open(settings_file, 'r', encoding="utf-8") as f:
                return yaml.safe_load(f)
        return {}

    @staticmethod
    def update_user_setting(key, value):
        settings_file = 'config/user_settings.yml'
        settings = UserSettings.load_user_settings()
        settings[key] = value
        with open(settings_file, 'w', encoding="utf-8") as f:
            yaml.dump(settings, f)