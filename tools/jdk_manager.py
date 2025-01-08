import os
import requests
import zipfile
import platform
import tarfile
from tkinter import filedialog, messagebox
import yaml


def save_config(config, config_path="config/config.yml"):
    try:
        with open(config_path, "w", encoding="utf-8") as file:
            yaml.dump(config, file, default_flow_style=False, allow_unicode=True)
        print(f"Конфигурация сохранена в {config_path}")
    except Exception as e:
        print(f"Ошибка при сохранении конфигурации: {e}")


class JDKManager:
    @staticmethod
    def install_jdk(version, config_path="config/config.yml"):
        system = platform.system().lower()
        
        if system == "windows":
            JDKManager._install_jdk_windows(version, config_path)
        elif system == "linux":
            JDKManager._install_jdk_linux(version, config_path)
        elif system == "darwin":
            JDKManager._install_jdk_macos(version, config_path)
        else:
            messagebox.showerror("Ошибка", f"Операционная система {system} не поддерживается.")

    @staticmethod
    def _install_jdk_windows(version, config_path):
        download_url = f"https://download.oracle.com/java/{version}/jdk-{version}_windows-x64_bin.zip"
        output_dir = filedialog.askdirectory(title="Выберите папку для установки JDK")
        if not output_dir:
            return

        try:
            response = requests.get(download_url, stream=True)
            zip_path = os.path.join(output_dir, f"jdk-{version}.zip")
            with open(zip_path, "wb") as zip_file:
                for chunk in response.iter_content(chunk_size=1024):
                    zip_file.write(chunk)

            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                zip_ref.extractall(output_dir)

            os.remove(zip_path)

            jdk_path = os.path.join(output_dir, f"jdk-{version}")
            JDKManager._update_config(config_path, jdk_path)

            messagebox.showinfo("Успех", f"JDK {version} успешно установлен в: {jdk_path}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось установить JDK {version} для Windows: {e}")

    @staticmethod
    def _install_jdk_linux(version, config_path):
        download_url = f"https://download.oracle.com/java/{version}/jdk-{version}_linux-x64_bin.tar.gz"
        output_dir = filedialog.askdirectory(title="Выберите папку для установки JDK")
        if not output_dir:
            return

        try:
            response = requests.get(download_url, stream=True)
            tar_path = os.path.join(output_dir, f"jdk-{version}.tar.gz")
            with open(tar_path, "wb") as tar_file:
                for chunk in response.iter_content(chunk_size=1024):
                    tar_file.write(chunk)

            with tarfile.open(tar_path, "r:gz") as tar_ref:
                tar_ref.extractall(output_dir)

            os.remove(tar_path)

            jdk_path = os.path.join(output_dir, f"jdk-{version}")
            JDKManager._update_config(config_path, jdk_path)

            messagebox.showinfo("Успех", f"JDK {version} успешно установлен в: {jdk_path}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось установить JDK {version} для Linux: {e}")

    @staticmethod
    def _install_jdk_macos(version, config_path):
        download_url = f"https://download.oracle.com/java/{version}/jdk-{version}_macos-x64_bin.dmg"
        output_dir = filedialog.askdirectory(title="Выберите папку для установки JDK")
        if not output_dir:
            return

        try:
            response = requests.get(download_url, stream=True)
            dmg_path = os.path.join(output_dir, f"jdk-{version}.dmg")
            with open(dmg_path, "wb") as dmg_file:
                for chunk in response.iter_content(chunk_size=1024):
                    dmg_file.write(chunk)

            messagebox.showinfo("Успех", f"Скачан .dmg файл JDK {version}. Установите его вручную.")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось установить JDK {version} для macOS: {e}")

    @staticmethod
    def set_jdk_path(config, config_path="config/config.yml"):
        jdk_path = filedialog.askdirectory(title="Выберите папку с установленным JDK")
        if jdk_path and JDKManager.is_valid_jdk_path(jdk_path):
            config["jdk_path"] = jdk_path
            save_config(config, config_path)
            messagebox.showinfo("Успех", f"Путь к JDK успешно сохранён: {jdk_path}")
        else:
            messagebox.showerror("Ошибка", "Указанный путь не является корректным JDK.")

    @staticmethod
    def is_valid_jdk_path(jdk_path):
        javac_path = os.path.join(jdk_path, "bin", "javac.exe" if os.name == "nt" else "javac")
        return os.path.exists(javac_path)

    @staticmethod
    def _update_config(config_path, jdk_path):
        with open(config_path, "r", encoding="utf-8") as file:
            config = yaml.safe_load(file)
        config["jdk_path"] = jdk_path
        save_config(config, config_path)
