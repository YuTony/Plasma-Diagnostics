import cv2

from ultralytics import YOLO

class PlasmaDetector():
    def __init__(self, model_path) -> None:
        self.model = YOLO(model_path)

    def predict(self, img):
        results = self.model(img)
        return results[0].plot()

