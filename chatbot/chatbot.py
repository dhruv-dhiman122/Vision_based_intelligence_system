# This file is for making chatbot system the core idea for it

from chatbot.learning import TrafficLearningSystem
from main import traffic_level


class TrafficChatbot:
    def __init__(self, counter, analyzer):
        self.counter = counter
        self.analyzer = analyzer
        self.learning = TrafficLearningSystem()

    def get_response(self, message: str) -> str:
        message_lower = message.lower()

        # learn from user message
        self.learning.process_message(message)

        total_count = getattr(self.counter, "total_count", 0)
        traffic_level = self.analyzer.get_traffic_level(total_count)

        if "traffic" in message_lower:
            return (
                f"Current traffic level is {traffic_level} with {total_count} vehicles"
            )

        elif "count" in message_lower or "vehicles" in message_lower:
            return f"Total vehicles detected: {total_count}"

        elif "insight" in message_lower or "summary" in message_lower:
            insights = self.learning.get_insights()
            return (
                f"Insight -> Heavy: {insights['heavy']}"
                f"Accidents: {insights['accident']}"
                f"Low: {insights['low']}"
            )

        elif "recent" in message_lower:
            recent = self.learning.get_recent()
            if not recent:
                return "No recent reports."
            return "\n".join([f"{r['location']}: {r['type']}" for r in recent])

        elif "high" in message_lower:
            if traffic_level.lower() == "high":
                return "Traffic is currently high"
            else:
                return "Traffic is not high right now"

        elif "help" in message_lower:
            return "You can ask about traffic level, vehicle count"

        else:
            return "I didnt understand. Try asking about traffic"
