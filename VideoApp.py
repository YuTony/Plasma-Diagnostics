import sys

import cv2
import numpy as np

from PySide6.QtCore import Signal, Slot, Qt, QThread
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtMultimedia import QMediaDevices

from VideoApp_ui import Ui_MainWindow


class VideoThread(QThread):
    change_pixmap_signal = Signal(np.ndarray)

    def __init__(self, camera):
        super().__init__()
        self._run_flag = True
        self._change_flag = False
        self.camera = camera

    def run(self):
        # capture from web cam
        cap = cv2.VideoCapture(self.camera)
        while self._run_flag:
            if self._change_flag:
                cap.release()
                cap = cv2.VideoCapture(self.camera)
                self._change_flag = False
            ret, cv_img = cap.read()
            if ret:
                self.change_pixmap_signal.emit(cv_img)
        # shut down capture system
        cap.release()

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()

    @Slot(int)
    def camera_select(self, camera):
        self.camera = camera
        self._change_flag = True


class PlasmaDiagnosticsApp(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.thread = VideoThread(0)
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)
        # start the thread
        self.thread.start()

        self.cameras = QMediaDevices.videoInputs()
        self.ui.cams_selector.currentIndexChanged.connect(self.thread.camera_select)
        self.ui.cams_selector.addItems(map(lambda c: c.description(), self.cameras))

    def closeEvent(self, event):
        self.thread.stop()
        event.accept()

    @Slot(np.ndarray)
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.ui.image_label.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(
            rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
        p = convert_to_Qt_format.scaled(
            self.ui.image_label.width(), self.ui.image_label.height(), Qt.AspectRatioMode.KeepAspectRatio)
        return QPixmap.fromImage(p)