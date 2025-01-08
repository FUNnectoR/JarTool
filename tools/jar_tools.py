import os
import subprocess
from tkinter import filedialog, messagebox


class JarTools:
    @staticmethod
    def decompile(config):
        jar_file = filedialog.askopenfilename(filetypes=[("JAR files", "*.jar")])
        if not jar_file:
            return
        
        fernflower = config.get("fernflower_path", "fernflower.jar")
        if not os.path.exists(fernflower):
            messagebox.showerror("Ошибка", f"Файл {fernflower} не найден.")
            return
        
        output_dir = filedialog.askdirectory()
        if not output_dir:
            return
        
        try:
            subprocess.run(["java", "-jar", fernflower, jar_file, output_dir], check=True)
            messagebox.showinfo("Успех", "Декомпиляция завершина!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка Декомпиляции: {e}")

    @staticmethod
    def compile(config):
        source_dir = filedialog.askdirectory()
        if not source_dir:
            return
        jar_file = filedialog.asksaveasfilename(defaultextension=".jar", filetypes=[("JAR files", "*.jar")])
        if not jar_file:
            return
        try:
            subprocess.run(["javac", "-d", source_dir, "*.java"], check=True)
            subprocess.run(["jar", "cvf", jar_file, "-C", source_dir, "."], check=True)
            messagebox.showinfo("Успех", "Компиляция завершена!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка компиляции: {e}")