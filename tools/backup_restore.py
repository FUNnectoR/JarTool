import shutil
import os
import datetime

class BackupRestore:
    @staticmethod
    def backup_files(source, destination):
        if os.path.exists(source):
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_dest = f"{destination}_{timestamp}"
            shutil.copytree(source, backup_dest)
            print(f"Резервная копия создана в {backup_dest}")
        else:
            print(f"Источник не найден: {source}")
    
    @staticmethod
    def restore_backup(backup_folder, destination):
        if os.path.exists(backup_folder):
            shutil.copytree(backup_folder, destination)
            print(f"Восстановление из {backup_folder} выполнено.")
        else:
            print(f"Резервная копия не найдена: {backup_folder}")