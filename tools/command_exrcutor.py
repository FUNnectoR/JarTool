import os
import subprocess
import platform
from tkinter import messagebox


class CommandExecutor:
    @staticmethod
    def execute_command(command):
        system = platform.system().lower()

        try:
            if system == "windows":
                CommandExecutor._execute_windows_command(command)
            elif system == "linux" or system == "darwin":
                CommandExecutor._execute_unix_command(command)
            else:
                messagebox.showerror("Ошибка", "Операционная система не поддерживается для выполнения команд.")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка выполнения команды: {e}")

    @staticmethod
    def _execute_windows_command(command):
        if command.endswith(".bat"):
            subprocess.run(command, shell=True)
        else:
            subprocess.run(command, shell=True)

    @staticmethod
    def _execute_unix_command(command):
        if command.endswith(".sh"):
            subprocess.run(["bash", command])
        else:
            subprocess.run(command, shell=True)