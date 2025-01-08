import os
from tkinter import filedialog, messagebox


class CodeAnalyzer:
    @staticmethod
    def analyze_code():
        folder_path = filedialog.askdirectory(title="Выберите папку с исходным кодом")
        if not folder_path:
            return

        total_lines = 0
        total_classes = 0
        total_methods = 0

        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".java"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "r") as f:
                        lines = f.readlines()
                        total_lines += len(lines)
                        total_classes += sum(1 for line in lines if "class " in line)
                        total_methods += sum(1 for line in lines if "void " in line or "public " in line)

        result = f"Общий код:\nСтрок: {total_lines}\nКлассов: {total_classes}\nМетодов: {total_methods}"
        messagebox.showinfo("Анализ кода", result)