# Made the file for senting notification to the user of this program

import requests
import time

class Notifier:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id
        self.last_sent_time = 0
        self.cooldown = 60 # seconds

    def sent_alert(self, message):
        current_time = time.time()

        # Prevents spams
        if current_time - self.last_sent_time < self.cooldown:
            return

        url = f"https//api.telegram.org/bot{self.token}/sendMessage"

        data = {
            "chat_id": self.chat_id,
            "text": message
        }

        try:
            requests.post(url, data = data)
            self.last_sent_time = current_time
        except:
            print("Failed to sent notification")
