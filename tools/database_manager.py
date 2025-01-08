import sqlite3
import os


class DatabaseManager:
    db_path = "data/app_data.db"

    @staticmethod
    def initialize_database():
        if not os.path.exists("data"):
            os.makedirs("data")
        conn = sqlite3.connect(DatabaseManager.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                status TEXT DEFAULT 'Pending',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS activity_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        conn.close()

    @staticmethod
    def add_task(title, description):
        conn = sqlite3.connect(DatabaseManager.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (title, description) VALUES (?, ?)", (title, description))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_tasks():
        conn = sqlite3.connect(DatabaseManager.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        conn.close()
        return tasks

    @staticmethod
    def update_task_status(task_id, status):
        conn = sqlite3.connect(DatabaseManager.db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, task_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_task(task_id):
        conn = sqlite3.connect(DatabaseManager.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def log_event(event):
        conn = sqlite3.connect(DatabaseManager.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO activity_logs (event) VALUES (?)", (event,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_logs():
        conn = sqlite3.connect(DatabaseManager.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM activity_logs")
        logs = cursor.fetchall()
        conn.close()
        return logs