import tkinter as tk
from tkinter import scrolledtext

class LogViewer:
    @staticmethod
    def open_logs():

        log_window = tk.Toplevel()
        log_window.title("Логи приложения")
        log_window.geometry("600x400")

        # Открываем файл логов
        with open("logs/app.log", "r", encoding="utf-8") as log_file:
            logs = log_file.read()

        # Создаем виджет для отображения логов
        log_text = scrolledtext.ScrolledText(log_window, wrap=tk.WORD, width=80, height=20)
        log_text.pack(padx=10, pady=10)
        log_text.insert(tk.INSERT, logs)
        log_text.config(state=tk.DISABLED)  # Отключаем редактирование

        log_window.mainloop()