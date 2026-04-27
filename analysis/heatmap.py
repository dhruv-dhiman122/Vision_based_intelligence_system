class HeatmapGenerator:
    def __init__(self, data_store):
        self.data_store = data_store

    def generate(self):
        df - self.data_store.df

        if df.empty:
            return {}

        weights = {
            "low" : 1,
            "heavy": 3,
            "accident": 5
        }

        df = df.copy()
        df["weight"] = df["event_type"].map(weights).fillna(1)

        heatmap = (
            df.groupby("location")["weight"]
            .sum()
            .to_dict()
        )
        return heatmap
