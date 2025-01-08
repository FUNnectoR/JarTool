import customtkinter as ctk

class ThemeManager:
    @staticmethod
    def switch_theme(theme: str):
        ctk.set_appearance_mode(theme)
        print(f"Тема переключена на: {theme}")

    @staticmethod
    def list_available_themes():
        return ["light", "dark", "system"]