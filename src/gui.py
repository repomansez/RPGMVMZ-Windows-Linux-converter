import sys
import os

from PySide6 import QtCore, QtWidgets

from convert import convert
from getnwjs import get_nwjs
from prechecks import check


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.selected_directory = None
        self.output_directory = None
        self.checks = None

        self.setWindowTitle("RPG Maker Converter")
        self.resize(700, 400)

        # Main layout
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
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

        # NW.js Version
        nwjs_label = QtWidgets.QLabel("NW.js Version")
        nwjs_label.setObjectName("section_label")

        self.nwjs_version = QtWidgets.QComboBox()

        view = QtWidgets.QListView()
        view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        view.setUniformItemSizes(True)

        self.nwjs_version.setView(view)

        self.nwjs_version.addItems(
            [
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
            ]
        )

        self.nwjs_version.setCurrentText("0.78.0")
        self.nwjs_version.setMaxVisibleItems(8)

        main_layout.addWidget(nwjs_label)
        main_layout.addWidget(self.nwjs_version)

        # Game Directory
        directory_label = QtWidgets.QLabel("Game Directory")
        directory_label.setObjectName("section_label")

        directory_layout = QtWidgets.QHBoxLayout()
        directory_layout.setSpacing(10)

        self.directory_edit = QtWidgets.QLineEdit()
        self.directory_edit.setPlaceholderText(
            "Select a game directory..."
        )
        self.directory_edit.setReadOnly(True)

        self.browse_button = QtWidgets.QPushButton("Browse")
        self.browse_button.setObjectName("browse_button")
        self.browse_button.setFixedWidth(100)

        directory_layout.addWidget(self.directory_edit)
        directory_layout.addWidget(self.browse_button)

        main_layout.addWidget(directory_label)
        main_layout.addLayout(directory_layout)

        # Output Directory
        output_directory_label = QtWidgets.QLabel("Output Directory")
        output_directory_label.setObjectName("section_label")

        output_directory_layout = QtWidgets.QHBoxLayout()
        output_directory_layout.setSpacing(10)

        self.output_directory_edit = QtWidgets.QLineEdit()
        self.output_directory_edit.setPlaceholderText(
            "Select an output directory..."
        )
        self.output_directory_edit.setReadOnly(True)

        self.output_browse_button = QtWidgets.QPushButton("Browse")
        self.output_browse_button.setObjectName(
            "output_browse_button"
        )
        self.output_browse_button.setFixedWidth(100)

        output_directory_layout.addWidget(
            self.output_directory_edit
        )
        output_directory_layout.addWidget(
            self.output_browse_button
        )

        main_layout.addWidget(output_directory_label)
        main_layout.addLayout(output_directory_layout)

        # Spacer
        main_layout.addStretch()

        # Conversion status
        self.status_label = QtWidgets.QLabel("")
        self.status_label.setObjectName("status_label")
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)

        main_layout.addWidget(self.status_label)

        # Timer for animated "Converting..."
        self.status_timer = QtCore.QTimer(self)
        self.status_timer.timeout.connect(self.update_status)
        self.status_dots = 0

        # Convert button
        self.convert_button = QtWidgets.QPushButton("Convert")
        self.convert_button.setObjectName("convert_button")
        self.convert_button.setMinimumHeight(50)

        main_layout.addWidget(self.convert_button)

        # Connections
        self.browse_button.clicked.connect(
            self.select_directory
        )

        self.output_browse_button.clicked.connect(
            self.select_directory_output
        )

        self.convert_button.clicked.connect(
            self.convert
        )

    @QtCore.Slot()
    def select_directory(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            "Select RPG Maker Game Directory",
        )

        if directory:
            self.selected_directory = directory
            self.directory_edit.setText(directory)

    @QtCore.Slot()
    def select_directory_output(self):
        output_directory = (
            QtWidgets.QFileDialog.getExistingDirectory(
                self,
                "Select Output Directory",
            )
        )

        if output_directory:
            self.output_directory = output_directory
            self.output_directory_edit.setText(
                output_directory
            )

    @QtCore.Slot()
    def update_status(self):
        self.status_dots = (self.status_dots + 1) % 5
        dots = "." * self.status_dots

        self.status_label.setText(
            f"Converting{dots}"
        )

    @QtCore.Slot()
    def convert(self):
        if not self.selected_directory:
            QtWidgets.QMessageBox.warning(
                self,
                "No Directory",
                "Please select the game directory.",
            )
            return

        elif not self.output_directory:
            QtWidgets.QMessageBox.warning(
                self,
                "No Directory",
                "Please select an output directory.",
            )
            return

        print(
            "Converting:",
            self.selected_directory,
            self.output_directory,
        )

        version = self.nwjs_version.currentText()
        gamepath = self.selected_directory
        gameoutput = self.output_directory

        version_status, dir_status = check(
            gamepath,
            gameoutput,
        )

        if dir_status == "notempty":
            subdir = os.path.basename(gamepath)

            self.gameoutput = os.path.join(
                gameoutput,
                subdir,
            )

            if not os.path.isdir(self.gameoutput):
                os.mkdir(self.gameoutput)

        if version_status == "not":
            QtWidgets.QMessageBox.information(
                self,
                "RPGM not detected",
                "No RPGM game detected in input.",
            )
            return

        elif dir_status == "notempty":
            QtWidgets.QMessageBox.information(
                self,
                "Output directory not empty",
                "The output directory should be empty, "
                "a subdirectory will be created.(soon)",
            )
            return

        if dir_status == "same":
            QtWidgets.QMessageBox.information(
                self,
                "Same directory",
                "Input and output directories cannot be "
                "the same.",
            )
            return

        elif version_status == "MV":
            QtWidgets.QMessageBox.information(
                self,
                "RPGMV",
                "RPGMV detected, will start conversion",
            )

        elif version_status == "MZ":
            QtWidgets.QMessageBox.information(
                self,
                "RPGMZ",
                "RPGMZ detected, will start conversion",
            )

        # Start animated status
        self.status_dots = 0
        self.status_label.setText("Converting")
        self.status_timer.start(400)

        # Disable controls while converting
        self.convert_button.setEnabled(False)
        self.browse_button.setEnabled(False)
        self.output_browse_button.setEnabled(False)
        self.nwjs_version.setEnabled(False)

        # Start worker thread
        self.worker = ConvertWorker(
            gamepath,
            gameoutput,
            version,
            version_status,
        )

        self.worker.finished.connect(
            self.conversion_finished
        )

        self.worker.start()

    @QtCore.Slot()
    def conversion_finished(self):
        # Stop animated status
        self.status_timer.stop()

        self.status_label.setText(
            "Conversion complete!"
        )

        # Re-enable controls
        self.convert_button.setEnabled(True)
        self.browse_button.setEnabled(True)
        self.output_browse_button.setEnabled(True)
        self.nwjs_version.setEnabled(True)

        QtWidgets.QMessageBox.information(
            self,
            "Conversion Complete",
            "The game was successfully converted!",
        )


class ConvertWorker(QtCore.QThread):
    finished = QtCore.Signal()

    def __init__(
        self,
        gamepath,
        gameoutput,
        version,
        version_status,
    ):
        super().__init__()

        self.gamepath = gamepath
        self.gameoutput = gameoutput
        self.version = version_status
        self.nwjs_version = version

    def run(self):
        get_nwjs(
            self.nwjs_version,
            self.gameoutput,
        )

        convert(
            self.gamepath,
            self.gameoutput,
            self.version,
        )

        self.finished.emit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    widget = MyWidget()
    widget.show()

    sys.exit(app.exec())