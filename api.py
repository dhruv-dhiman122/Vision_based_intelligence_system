import cv2
from flask import Flask, Response, render_template

from analysis.traffic_analysis import TrafficAnalyzer
from main import analyzer, detector
from src.camera_file import VehicleDetector
from src.vehicle_counter import VehicleCounter
from utils.notifier import Notifier

api = Flask(__name__)

# init module
detector = VehicleDetector()
counter = VehicleCounter(line_position=300)
analyzer = TrafficAnalyzer()

notifier = Notifier("YOUR_TOKEN", "CHAT_ID")

cap = cv2.VideoCapture("video2.mp4")

frame_count = 0


def generate_frames():
    global frame_count

    while True:
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.resize(frame, (800, 600))

        # AI detection
        detections = detector.detect(frame)

        # counting
        total_count = counter.update(detections)

        # analysis
        if frame_count % 30 == 0:
            analyzer.log_data(total_count)

        traffic_level = analyzer.get_traffic_level(total_count)

        # notification
        if total_count > 30:
            notifier.sent_alert(f"High traffic detected: {total_count}")

        # Draw line
        cv2.line(frame, (0, 300), (800, 300), (0, 0, 255), 2)

        # Draw box
        for det in detections:
            x1, y1, x2, y2 = det["bbox"]
            label = det["label"]
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(
                frame,
                label,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                2,
            )

        # text info
        cv2.putText(
            frame,
            f"Count: {total_count}",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
            2,
        )

        cv2.putText(
            frame,
            f"Traffic: {traffic_level}",
            (20, 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 255),
            2,
        )
