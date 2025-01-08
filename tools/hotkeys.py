import customtkinter as ctk

class Hotkeys:
    @staticmethod
    def set_hotkeys(root):
        root.bind("<Control-Shift-D>", lambda event: print("Декомпиляция JAR (быстрая команда)"))
        root.bind("<Control-Shift-C>", lambda event: print("Компиляция JAR (быстрая команда)"))
        root.bind("<Control-Shift-E>", lambda event: print("Сборка EXE (быстрая команда)"))