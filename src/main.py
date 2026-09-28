import sys
from PySide6 import QtWidgets
from gui import MyWidget
from pathlib import Path


def main():
    app = QtWidgets.QApplication(sys.argv)
    style_path = Path(__file__).parent / "style.qss"
    with open(style_path, "r") as f:
        app.setStyleSheet(f.read())
    widget = MyWidget()
    widget.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
