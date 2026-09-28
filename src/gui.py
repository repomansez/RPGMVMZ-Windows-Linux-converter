import sys
from getnwjs import get_nwjs
from convert import convert
from PySide6 import QtCore, QtWidgets
#from prechecks import check


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.selected_directory = None
        self.selected_directory = None
        self.output_directory = None
        self.output_directory = None
        

        self.setWindowTitle("RPG Maker Converter")
        self.resize(700, 400)

        # Main layout
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)
        nwjs_label = QtWidgets.QLabel("NW.js Version")
        nwjs_label.setObjectName("section_label")

        # Title
        title = QtWidgets.QLabel("RPG Maker Converter")
        title.setObjectName("title")

        subtitle = QtWidgets.QLabel(
            "Select an RPG Maker game directory to begin."
        )
        subtitle.setObjectName("subtitle")

        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)

        self.nwjs_version = QtWidgets.QComboBox()
        view = QtWidgets.QListView()
        view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        view.setUniformItemSizes(True)
        self.nwjs_version.setView(view)
        
        self.nwjs_version.addItems([
            # Older / RPG Maker compatibility
            "0.29.4",
            "0.44.5",
            "0.48.4",
            "0.59.1",
            "0.67.1",
            "0.69.1",
            "0.78.0",
        
            # Modern
            "0.93.0",
            "0.94.0",
            "0.110.1",
            "0.111.3",
            "0.112.0",
            "0.113.0",
            "0.114.2",
            "0.115.0",
            "0.116.0",
            "0.117.0",
        ])
        
        self.nwjs_version.setCurrentText("0.78.0")
        self.nwjs_version.setMaxVisibleItems(8)
        
        
        main_layout.addWidget(nwjs_label)
        main_layout.addWidget(self.nwjs_version)
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

        # Output Directory selector
       # title = QtWidgets.QLabel("RPG Maker Converter")
       # title.setObjectName("title")

        subtitle = QtWidgets.QLabel(
            "Select an RPG Maker game directory to begin."
        )

         # Directory section
        output_directory_label = QtWidgets.QLabel("Output Directory")
        output_directory_label.setObjectName("section_label")

        output_directory_layout = QtWidgets.QHBoxLayout()
        output_directory_layout.setSpacing(10)

        self.output_directory_edit = QtWidgets.QLineEdit()
        self.output_directory_edit.setPlaceholderText("Select an output directory...")
        self.output_directory_edit.setReadOnly(True)

        self.output_browse_button = QtWidgets.QPushButton("Browse")
        self.output_browse_button.setObjectName("output_browse_button")
        self.output_browse_button.setFixedWidth(100)

        output_directory_layout.addWidget(self.output_directory_edit)
        output_directory_layout.addWidget(self.output_browse_button)

        main_layout.addWidget(output_directory_label)
        main_layout.addLayout(output_directory_layout)

        # # Spacer
        main_layout.addStretch()

        # Convert button
        self.convert_button = QtWidgets.QPushButton("Convert")
        self.convert_button.setObjectName("convert_button")
        self.convert_button.setMinimumHeight(50)

        main_layout.addWidget(self.convert_button)

        # Connections
        self.browse_button.clicked.connect(self.select_directory)
        #self.browse_button.clicked.connect(self.select_directory_output)
        self.output_browse_button.clicked.connect(self.select_directory_output)
        
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
    def select_directory_output(self):
        output_directory = QtWidgets.QFileDialog.getExistingDirectory(
         self,
             "Select Output Directory"
         )
        if output_directory:
             self.output_directory = output_directory
             self.output_directory_edit.setText(output_directory)

    @QtCore.Slot()
    def convert(self):
        if not self.selected_directory:
            QtWidgets.QMessageBox.warning(
                self,
                "No Directory",
                "Please select the game directory."
            )
            return
        elif not self.output_directory:
            QtWidgets.QMessageBox.warning(
                self,
                "No Directory",
                "Please select an output directory."
            )            
            return


        # Your converter function goes here
        print("Converting:", self.selected_directory, self.output_directory)
        version = self.nwjs_version.currentText()
        gamepath = self.selected_directory 
        gameoutput = self.output_directory
        check()
        get_nwjs(version, gameoutput)
        convert(gamepath, gameoutput)
        QtWidgets.QMessageBox.information(
        self,
        "Conversion Complete",
        "The game was successfully converted!"
    )


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    widget = MyWidget()
    widget.show()

    sys.exit(app.exec())