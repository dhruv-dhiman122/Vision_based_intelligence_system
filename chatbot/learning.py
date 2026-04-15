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
