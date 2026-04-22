# The aim of this file is show differnt type
# of vehcile and their count


class VehicleStats:
    def __init__(self):
        self.counts = {}

    def update(self, detections):
        for det in detections:
            label = det.get("label", "unkown")

            if label not in self.counts:
                self.counts[label] = 0

            self.counts[label] += 1
