import cv2

from src.camera_file import VehicleDetector
from src.vehicle_counter import VehicleCounter
from analysis.traffic_analysis import TrafficAnalyzer
from utils.notifier import Notifier

#Initialize modules
detector = VehicleDetector()
counter = VehicleCounter(line_position=300)
analyzer = TrafficAnalyzer()

# TODO -> to replace with my telegram bot details
# notifier = Notifier("token", "my chat id")
cap = cv2.VideoCapture("video.mp4")

if not cap.isOpened():
    print("Error: Cannot open video")
    exit();

frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (800, 600))
    detections = detector.detect(frame)

    # Update counter
    total_count = counter.update(detections)

    # draw line
    cv2.line(frame, (0, 300), (800, 300), (0, 0, 255), 2)

    for det in detections:
        x1, y1, x2, y2 = det["bbox"]
        label = det["label"]
        conf = det["confidence"]

        # Drawing bounding box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(
            frame,
            f"{label} {conf:.2f}",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            2,
        )

    # Display count
    cv2.putText(
        frame,
        f"Vehicle Count: {total_count}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2,
    )
    cv2.imshow("Vehicle Detection", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
