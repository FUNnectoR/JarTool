import threading
from tkinter import messagebox

class TaskManager:
    @staticmethod
    def run_in_background(task, *args):
        thread = threading.Thread(target=task, args=args)
        thread.start()
    
    @staticmethod
    def show_task_completed_message():
        messagebox.showinfo("Задача выполнена", "Операция завершена успешно.")