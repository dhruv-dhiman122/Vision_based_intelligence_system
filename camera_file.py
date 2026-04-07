from ultralytics import YOLO
import cv2

class VehicleDetector:
    def __init__(self, model_path="yolov8n.pt"):
        self.model = YOLO(model_path)

        self.vehicle_classes = [
            "car", "motorcycle", "bus", "truck", "bicycle"
        ]

    def detect(self, frame):
        results = self.model(frame)

        detections = []

        for result in results:
            for box in result.boxes:
                cls_id = int(box.cls[0])
                label = self.model.names[cls_id]

                if label in self.vehicle_classes:
                    x1,y1,x2,y2 = map(int, box.xyxy[0])
                    conf = float(box.conf[0])

                    detections.append({
                        "label": label,
                        "confidence": conf,
                        "bbox" : (x1,y1, x2, y2)
                    })
        return detections
