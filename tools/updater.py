import requests
import os
from tkinter import messagebox


class Updater:
    @staticmethod
    def check_for_updates(config):
        current_version = config.get("version", "1.0.0")
        version_url = "https://raw.githubusercontent.com/FUNnectoR/JarTool/main/config/version.jartool"
        download_url = "https://github.com/FUNnectoR/JarTool/archive/refs/heads/main.zip"

        try:
            response = requests.get(version_url)
            response.raise_for_status()
            latest_version = response.text.strip()

            if latest_version > current_version:
                messagebox.showinfo(
                    "Обновление доступно",
                    f"Доступна новая версия: {latest_version}\n\nТекущая версия: {current_version}\n"
                    f"Обновление будет загружено и установлено.",
                )
                Updater.download_and_extract_update(download_url, latest_version)
            else:
                messagebox.showinfo("Обновление", "У вас установлена последняя версия.")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Ошибка", f"Не удалось проверить обновления: {e}")

    @staticmethod
    def download_and_extract_update(download_url, new_version):
        try:
            response = requests.get(download_url, stream=True)
            response.raise_for_status()

            zip_path = "update.zip"
            with open(zip_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

            import zipfile
            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                zip_ref.extractall("update_temp")

            Updater.replace_files("update_temp/JarTool-main", os.getcwd())

            os.remove(zip_path)
            import shutil
            shutil.rmtree("update_temp")

             Updater.update_version(new_version)
            messagebox.showinfo("Обновление", "Приложение успешно обновлено!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить или установить обновление: {e}")

    @staticmethod
    def replace_files(source_dir, target_dir):
        import shutil
        for item in os.listdir(source_dir):
            src_path = os.path.join(source_dir, item)
            tgt_path = os.path.join(target_dir, item)

            if os.path.isdir(src_path):
                if os.path.exists(tgt_path):
                    shutil.rmtree(tgt_path)
                shutil.copytree(src_path, tgt_path)
            else:
                shutil.copy2(src_path, tgt_path)

    @staticmethod
    def update_version(new_version):
        version_file = 'config/version.jartool'
        try:
            with open(version_file, 'w') as f:
                f.write(new_version)
            print(f"Версия обновлена до {new_version}")
        except Exception as e:
            print(f"Не удалось обновить версию: {e}")