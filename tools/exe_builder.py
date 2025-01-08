import subprocess
from tkinter import filedialog, messagebox


class ExeBuilder:
    @staticmethod
    def build_exe():
        script_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
        if not script_path:
            return
        icon_path = filedialog.askopenfilename(filetypes=[("Icon files", "*.ico"), ("All files", "*.*")])
        output_dir = filedialog.askdirectory()
        if not output_dir:
            return

        command = ["pyinstaller", "--onefile", "--distpath", output_dir]
        if icon_path:
            command.extend(["--icon", icon_path])
        command.append(script_path)

        try:
            subprocess.run(command, check=True)
            messagebox.showinfo("Успех", f"Сборка EXE завершена! Файл сохранен в: {output_dir}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка сборки EXE: {e}")