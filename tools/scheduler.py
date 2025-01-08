import time
import threading

class Scheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_function, delay_seconds):
        task = threading.Timer(delay_seconds, task_function)
        self.tasks.append(task)
        task.start()

    def cancel_all(self):
        for task in self.tasks:
            task.cancel()