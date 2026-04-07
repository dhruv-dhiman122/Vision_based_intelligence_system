import numpy as np


class VehicleCounter:
    def __init__(self, line_position=300):
        self.line_position = line_position
        self.count = 0

        # to reduce double counting
        self.offset = 10
        self.already_counted = []

    def get_center(self, bbox):
        x1, y1, x2, y2 = bbox
        cx = int((x1 + y1) / 2)
        cy = int((x2 + y2) / 2)
        return cx, cy

    def update(self, detections):
        new_centers = []

        for det in detections:
            cx, cy = self.get_center(det["bbox"])
            new_centers.append((cx, cy))

            # Check if corssing the line
            if (
                (self.line_position - self.offset)
                < cy
                < (self.line_position + self.offset)
            ):
                if (cx, cy) not in self.already_counted:
                    self.count += 1
                    self.already_counted.append((cx, cy))

        # clean old points
        if len(self.already_counted) > 100:
            self.already_counted = self.already_counted[-50:]

        return self.count
