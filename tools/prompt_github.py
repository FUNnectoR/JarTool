import threading
import webbrowser
from tkinter import messagebox

class GitHubPrompt:
    @staticmethod
    def start_timer(root, github_url, delay_minutes=10):
        delay_seconds = delay_minutes * 60
        threading.Timer(delay_seconds, GitHubPrompt.show_prompt, args=(root, github_url)).start()

    @staticmethod
    def show_prompt(root, github_url):
        def open_github():
            webbrowser.open(github_url)
        response = messagebox.askyesno(
            "Оцените нас на GitHub",
            "Вы пользуетесь приложением уже 10 минут. Хотите оценить нас на GitHub?",
        )
        if response:
            open_github()