from tkinter import Toplevel, Label, Entry, Button, Listbox
from tools.database_manager import DatabaseManager


class TaskManagerUI:
    @staticmethod
    def open_task_manager(root):
        task_window = Toplevel(root)
        task_window.title("Управление задачами")
        task_window.geometry("500x400")

        Label(task_window, text="Название задачи").pack(pady=5)
        title_entry = Entry(task_window, width=40)
        title_entry.pack(pady=5)

        Label(task_window, text="Описание задачи").pack(pady=5)
        desc_entry = Entry(task_window, width=40)
        desc_entry.pack(pady=5)

        def add_task():
            title = title_entry.get()
            description = desc_entry.get()
            DatabaseManager.add_task(title, description)
            update_task_list()

        Button(task_window, text="Добавить задачу", command=add_task).pack(pady=5)

        task_listbox = Listbox(task_window, width=50, height=15)
        task_listbox.pack(pady=10)

        def update_task_list():
            task_listbox.delete(0, 'end')
            tasks = DatabaseManager.get_all_tasks()
            for task in tasks:
                task_listbox.insert('end', f"#{task[0]} {task[1]} [{task[3]}]")

        def complete_task():
            selected = task_listbox.curselection()
            if selected:
                task_id = task_listbox.get(selected).split()[0][1:]
                DatabaseManager.update_task_status(task_id, "Completed")
                update_task_list()

        Button(task_window, text="Завершить задачу", command=complete_task).pack(pady=5)
        update_task_list()