import sys
import traceback
from tkinter import messagebox
import customtkinter as ctk

# Импорт
from tools.jar_tools import JarTools
from tools.exe_builder import ExeBuilder
from tools.jdk_manager import JDKManager
from tools.code_editor import CodeEditor
from tools.updater import Updater
from tools.utils import load_config, load_language, setup_logging
from tools.user_settings import UserSettings
from tools.error_reporter import ErrorReporter
from tools.backup_restore import BackupRestore
from tools.jar_search import JarSearch
from tools.hotkeys import Hotkeys
from tools.autostart import AutoStart
from tools.resource_monitor import ResourceMonitor
from tools.file_encryptor import FileEncryptor
from tools.task_manager import TaskManager
from tools.plugin_manager import PluginManager
from tools.theme_manager import ThemeManager
from tools.network_checker import NetworkChecker
from tools.log_cleaner import LogCleaner
from tools.database_manager import DatabaseManager
from tools.prompt_github import GitHubPrompt


def global_exception_handler(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.excepthook(exc_type, exc_value, exc_traceback)
        return
    ErrorReporter.generate_report(exc_value)
    print(f"Произошла ошибка: {exc_value}")
    traceback.print_tb(exc_traceback)


sys.excepthook = global_exception_handler


class JarToolApp:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Jar Tool")
        self.root.geometry("900x700")
        self.root.resizable(False, False)

        try:
            self.config = load_config()
            self.language = load_language(self.config.get("language", "config/lang_ru.yml"))
            setup_logging(self.config.get("log_file", "logs/app.log"))

            DatabaseManager.initialize_database()

            ThemeManager.switch_theme(self.config.get("theme", "dark"))

            self.user_settings = UserSettings.load_user_settings()

            self.plugins = PluginManager.load_plugins()

            LogCleaner.clean_logs()

            AutoStart.add_to_autostart()

            if not NetworkChecker.is_connected():
                messagebox.showwarning("Предупреждение", "Нет подключения к интернету.")

            GitHubPrompt.start_timer(self.root, github_url="https://github.com/FUNnectoR")

            self.create_main_menu()

        except Exception as e:
            ErrorReporter.generate_report(e)
            messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

    def create_main_menu(self):
        label = ctk.CTkLabel(self.root, text="Jar Tool", font=("Arial", 24))
        label.pack(pady=20)

        buttons = [
            ("Декомпиляция JAR", self.decompile_jar),
            ("Компиляция JAR", self.compile_jar),
            ("Редактор кода", self.open_code_editor),
            ("Сборка EXE", self.build_exe),
            ("Настроить JDK", self.manage_jdk),
            ("Резервное копирование", self.backup_files),
            ("Обновления", self.check_updates),
            ("Использование ресурсов", self.show_resources),
            ("Шифрование файлов", self.encrypt_config),
            ("Запуск задач", self.run_tasks),
            ("Переключить тему", self.switch_theme),
            ("Поиск JAR файлов", self.search_jars),
            ("Выход", self.exit_app),
        ]

        for text, command in buttons:
            btn = ctk.CTkButton(self.root, text=text, command=command)
            btn.pack(pady=10)

        Hotkeys.set_hotkeys(self.root)

    def decompile_jar(self):
        JarTools.decompile(self.config)
        messagebox.showinfo("Инфо", "Декомпиляция JAR завершена.")

    def compile_jar(self):
        JarTools.compile(self.config)
        messagebox.showinfo("Инфо", "Компиляция JAR завершена.")

    def open_code_editor(self):
        CodeEditor.open_editor(self.root)

    def build_exe(self):
        ExeBuilder.build_exe()

    def manage_jdk(self):
        JDKManager.set_jdk_path()
        messagebox.showinfo("Инфо", "JDK настроен.")

    def backup_files(self):
        BackupRestore.backup_files("config", "backups")
        messagebox.showinfo("Инфо", "Резервное копирование завершено.")

    def check_updates(self):
        Updater.check_for_updates(self.config)
        messagebox.showinfo("Инфо", "Проверка обновлений завершена.")

    def show_resources(self):
        cpu = ResourceMonitor.get_cpu_usage()
        ram = ResourceMonitor.get_memory_usage()
        disk = ResourceMonitor.get_disk_usage()
        messagebox.showinfo("Использование ресурсов", f"CPU: {cpu}%\nRAM: {ram[0]:.2f}/{ram[1]:.2f} MB\nDisk: {disk}%")

    def encrypt_config(self):
        key = FileEncryptor.generate_key()
        FileEncryptor.encrypt_file("config/user_config.yml", key)
        messagebox.showinfo("Шифрование", "Файл конфигурации зашифрован.")

    def run_tasks(self):
        TaskManager.run_in_background(self.dummy_task)
        messagebox.showinfo("Инфо", "Задача запущена.")

    def dummy_task(self):
        import time
        for i in range(5):
            print(f"Выполняется задача: шаг {i + 1}")
            time.sleep(1)

    def switch_theme(self):
        current_theme = self.config.get("theme", "dark")
        new_theme = "light" if current_theme == "dark" else "dark"
        self.config["theme"] = new_theme
        ThemeManager.switch_theme(new_theme)
        messagebox.showinfo("Тема", f"Тема переключена на {new_theme}.")

    def search_jars(self):
        jar_files = JarSearch.search_jars(".")
        messagebox.showinfo("Результаты поиска", f"Найденные JAR файлы: {', '.join(jar_files)}")

    def exit_app(self):
        self.root.quit()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = JarToolApp()
    app.run()
