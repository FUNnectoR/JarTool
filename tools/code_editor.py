import tkinter as tk
from tkinter import filedialog, messagebox


class CodeEditor:
    @staticmethod
    def open_editor(root):
        editor_window = tk.Toplevel(root)
        editor_window.title("Редактор кода")

        text_area = tk.Text(editor_window, wrap=tk.WORD, font=("Arial", 12))
        text_area.pack(fill=tk.BOTH, expand=True)

        toolbar = tk.Frame(editor_window)
        toolbar.pack(fill=tk.X)

        open_button = tk.Button(toolbar, text="Открыть", command=lambda: CodeEditor.open_file(text_area))
        open_button.pack(side=tk.LEFT)

        save_button = tk.Button(toolbar, text="Сохранить", command=lambda: CodeEditor.save_file(text_area))
        save_button.pack(side=tk.LEFT)

        clear_button = tk.Button(toolbar, text="Очистить", command=lambda: CodeEditor.clear_text(text_area))
        clear_button.pack(side=tk.LEFT)

        editor_window.geometry("800x600")

    @staticmethod
    def open_file(text_area):
        file_path = filedialog.askopenfilename(defaultextension=".java", filetypes=[("Java files", "*.java")])
        if file_path:
            with open(file_path, "r") as file:
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, file.read())

    @staticmethod
    def save_file(text_area):
        file_path = filedialog.asksaveasfilename(defaultextension=".java", filetypes=[("Java files", "*.java")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(text_area.get(1.0, tk.END))
            messagebox.showinfo("Успех", "Файл успешно сохранен!")

    @staticmethod
    def clear_text(text_area):
        text_area.delete(1.0, tk.END)