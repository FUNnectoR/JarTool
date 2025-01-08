import os
import time

class LogCleaner:
    @staticmethod
    def clean_logs(log_directory="logs", max_age_days=7):
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

            now = time.time()
            for file in os.listdir(log_directory):
                file_path = os.path.join(log_directory, file)

                if os.path.isfile(file_path):
                    file_age = (now - os.path.getmtime(file_path)) / 86400
                    if file_age > max_age_days:
                        os.remove(file_path)
                        print(f"Лог {file} удалён, так как он старше {max_age_days} дней.")