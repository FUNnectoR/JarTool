import os
import sys
import platform

class AutoStart:
    @staticmethod
    def add_to_autostart():
        if platform.system() == "Windows":
            python_executable = sys.executable
            script_path = os.path.abspath("main.py")
            shortcut = f"\"{python_executable}\" \"{script_path}\""
            
            autostart_folder = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
            shortcut_file = os.path.join(autostart_folder, "JarTool.lnk")
            
            with open(shortcut_file, "w") as f:
                f.write(shortcut)
            
            print("Программа добавлена в автозагрузку.")
        else:
            print("Поддержка автозагрузки только для Windows.")
