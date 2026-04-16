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
