from datetime import datetime

import pandas as pd


class TrafficDataStore:
    def __init__(self):
        self.df = pd.DataFrame(
            columns=[
                "timestamp",
                "location",
                "event_type",  # accident/heavy/low
                "source",
            ]
        )

    def add_event(self, location, event_type, source="AI"):
        new_row = {
            "timestamp": datetime.now(),
            "location": location,
            "event_type": event_type,
            "source": source,
        }

        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)

    def get_summary(self):
        return self.df["event_type"].value_counts().to_dict()

    def get_hourly_traffic(self):
        self.df["hour"] = self.df["timestamp"].dt.hour
        return self.df.groupby("hour").size()

    def export_csv(self, filename="traffic_data.csv"):
        self.df.to_csv(filename, index=False)
