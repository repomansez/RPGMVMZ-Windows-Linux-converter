import sys
from getnwjs import get_nwjs
from convert import convert
from PySide6 import QtCore, QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.selected_directory = None

        self.setWindowTitle("RPG Maker Converter")
        self.resize(700, 400)

        # Main layout
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(40, 40, 40, 40)
        main_layout.setSpacing(20)

        # Title
        title = QtWidgets.QLabel("RPG Maker Converter")
        title.setObjectName("title")

        subtitle = QtWidgets.QLabel(
            "Select an RPG Maker game directory to begin."
        )
        subtitle.setObjectName("subtitle")

        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)

        # Directory section
        directory_label = QtWidgets.QLabel("Game Directory")
        directory_label.setObjectName("section_label")

        directory_layout = QtWidgets.QHBoxLayout()
        directory_layout.setSpacing(10)

        self.directory_edit = QtWidgets.QLineEdit()
        self.directory_edit.setPlaceholderText("Select a game directory...")
        self.directory_edit.setReadOnly(True)

        self.browse_button = QtWidgets.QPushButton("Browse")
        self.browse_button.setObjectName("browse_button")
        self.browse_button.setFixedWidth(100)

        directory_layout.addWidget(self.directory_edit)
        directory_layout.addWidget(self.browse_button)

        main_layout.addWidget(directory_label)
        main_layout.addLayout(directory_layout)

        # Spacer
        main_layout.addStretch()

        # Convert button
        self.convert_button = QtWidgets.QPushButton("Convert")
        self.convert_button.setObjectName("convert_button")
        self.convert_button.setMinimumHeight(50)

        main_layout.addWidget(self.convert_button)

        # Connections
        self.browse_button.clicked.connect(self.select_directory)
        self.convert_button.clicked.connect(self.convert)

        # Styling
        self.setStyleSheet("""
            QWidget {
                background-color: #111111;
                color: #dddddd;
                font-size: 14px;
            }

            QLabel#title {
                font-size: 28px;
                font-weight: bold;
                color: #ffffff;
            }

            QLabel#subtitle {
                color: #888888;
                font-size: 14px;
            }

            QLabel#section_label {
                color: #aaaaaa;
                font-size: 13px;
            }

            QLineEdit {
                background-color: #1b1b1b;
                border: 1px solid #333333;
                border-radius: 6px;
                padding: 10px;
                color: #dddddd;
            }

            QLineEdit:focus {
                border: 1px solid #666666;
            }

            QPushButton {
                background-color: #222222;
                border: 1px solid #444444;
                border-radius: 6px;
                padding: 10px 16px;
                color: #dddddd;
            }

            QPushButton:hover {
                background-color: #2c2c2c;
            }

            QPushButton:pressed {
                background-color: #181818;
            }

            QPushButton#convert_button {
                background-color: #dddddd;
                color: #111111;
                border: none;
                font-size: 16px;
                font-weight: bold;
            }

            QPushButton#convert_button:hover {
                background-color: #ffffff;
            }

            QPushButton#convert_button:pressed {
                background-color: #aaaaaa;
            }
        """)

    @QtCore.Slot()
    def select_directory(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            "Select RPG Maker Game Directory"
        )

        if directory:
            self.selected_directory = directory
            self.directory_edit.setText(directory)

    @QtCore.Slot()
    def convert(self):
        if not self.selected_directory:
            QtWidgets.QMessageBox.warning(
                self,
                "No Directory",
                "Please select an RPG Maker game directory first."
            )
            return

        # Your converter function goes here
        print("Converting:", self.selected_directory)
        version = "0.78.0"
        gamepath = self.selected_directory ####### TO BE SET BY GUI LATER
        get_nwjs(version)
        convert(gamepath)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    widget = MyWidget()
    widget.show()

    sys.exit(app.exec())