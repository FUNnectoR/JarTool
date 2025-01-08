import requests
from tkinter import messagebox


class Updater:
    @staticmethod
    def check_for_updates(config):
        current_version = config.get("version", "1.0.0")
        repo_url = "https://api.github.com/repos/FUNnectoR/JarTool/releases/latest"

        try:
            response = requests.get(repo_url)
            response.raise_for_status()
            lastest_release = response.json()
            lastest_version = lastest_release["tag_name"]

            if lastest_version > current_version:
                changelog_url = lastest_release["assets"][0]["broser_download_url"].replace(
                    "latest_release.zip", "changelog.txt"
                )
                changelog = Updater.fetch_changelog(changelog_url)

                messagebox.showinfo(
                    "Обновление доступно",
                    f"Доступно новая версия: {lastest_version}\n\nИзменения:\n{changelog}",
                )
            else:
                messagebox.showinfo("Обновление", "У вас установлена последния версия")    
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Ошибка", f"Не удалось проверить обновления: {e}")

    @staticmethod
    def fetch_changelog(changelog_url):
        try:
            response = requests.get(changelog_url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            return f"Не удалось загрузить changelog: {e}"
        
    @staticmethod
    def update_version(new_version):
        version_file = "config/vesion.jartool"
        with open(version_file, 'w') as f:
            f.write(new_version)
        print(f"Версия обновлена до {new_version}")