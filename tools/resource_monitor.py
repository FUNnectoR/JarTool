import psutil

class ResourceMonitor:
    @staticmethod
    def get_cpu_usage():
        return psutil.cpu_percent(interval=1)

    @staticmethod
    def get_memory_usage():
        mem = psutil.virtual_memory()
        return mem.used / (1024 ** 2), mem.total / (1024 ** 2)

    @staticmethod
    def get_disk_usage():
        return psutil.disk_usage('/').percent