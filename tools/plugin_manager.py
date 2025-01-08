import os
import importlib

class PluginManager:
    @staticmethod
    def load_plugins(plugin_directory="plugins"):
        if not os.path.exists(plugin_directory):
            os.makedirs(plugin_directory)
            print("Папка для плагинов создана.")

        plugins = []
        for file in os.listdir(plugin_directory):
            if file.endswith(".py"):
                module_name = file[:-3]
                try:
                    module = importlib.import_module(f"{plugin_directory}.{module_name}")
                    plugins.append(module)
                except Exception as e:
                    print(f"Ошибка загрузки плагина {module_name}: {e}")
        return plugins