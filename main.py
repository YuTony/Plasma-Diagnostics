import sys

from PySide6 import QtWidgets

from VideoApp import PlasmaDiagnosticsApp


def main():
    app = QtWidgets.QApplication(sys.argv)

    video_app = PlasmaDiagnosticsApp()
    # server_app.setWindowTitle("Server")
    # server_app.resize(400, 300)
    # server_app.move(10, 50)
    video_app.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
