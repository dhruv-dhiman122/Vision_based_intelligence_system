# This file is for making chatbot system the core idea for it

from main import traffic_level


class TrafficChatbot:
    def __init__(self, counter, analyzer):
        self.counter = counter
        self.analyzer = analyzer

    def get_response(self, message: str) -> str:
        message = message.lower()

        total_count = getattr(self.counter, "total_count", 0)
        traffic_level = self.analyzer.get_traffic_level(total_count)

        if "traffic" in message:
            return (
                f"Current traffic level is {traffic_level} with {total_count} vehicles"
            )

        elif "count" in message or "vehicles" in message:
            return f"Total vehicles detected: {total_count}"

        elif "high" in message:
            if traffic_level.lower() == "high":
                return "Traffic is currently high"
            else:
                return "Traffic is not high right now"

        elif "help" in message:
            return "You can ask about traffic level, vehicle count"

        else:
            return "I didnt understand. Try asking about traffic"
