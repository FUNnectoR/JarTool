import json
from datetime import datetime

class UserAnalytics:
    stats_file = "analytics/stats.json"

    @staticmethod
    def log_event(event_name: str):
        data = {"event": event_name, "timestamp": str(datetime.now())}
        with open(UserAnalytics.stats_file, "a") as file:
            json.dump(data, file)
            file.write("\n")
        print(f"Событие '{event_name}' зафиксировано.")