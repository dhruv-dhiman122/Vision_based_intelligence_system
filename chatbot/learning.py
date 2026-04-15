# This is the file that used for learning from the message user make about traffic


class TrafficLearningSystem:
    def __init__(self):
        self.learned_data = []

    def process_message(self, message: str, location: str = "Unknown"):
        message = message.lower()

        traffic_type = None

        if "accident" in message:
            traffic_type = "accident"
        elif "jam" in message or "traffic" in message:
            traffic_type = "heavy"
        elif "clear" in message:
            traffic_type = "low"

        if traffic_type:
            data = {"location": location, "type": traffic_type, "message": message}
            self.learned_data.append(data)
            return data

        return None

    def get_insights(self):
        summary = {"accident": 0, "heavy": 0, "low": 0}

        for d in self.learned_data:
            summary[d["type"]] += 1

        return summary

    def get_recent(self, limit=5):
        return self.learned_data[-limit:]
