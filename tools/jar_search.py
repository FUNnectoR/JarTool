import os

class JarSearch:
    @staticmethod
    def search_jars(directory):
        jar_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.jar'):
                    jar_files.append(os.path.join(root, file))
        return jar_files