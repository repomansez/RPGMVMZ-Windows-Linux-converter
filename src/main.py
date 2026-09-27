#import os
#from getnwjs import get_nwjs
#from convert import convert

#def main():
#    version = "0.78.0"
#    gamepath = "oe" ####### TO BE SET BY GUI LATER
#    get_nwjs(version)
#    convert(gamepath)

#if __name__ == "__main__":
#    main()

import sys
from PySide6 import QtWidgets
from gui import MyWidget


def main():
    app = QtWidgets.QApplication(sys.argv)

    widget = MyWidget()
    widget.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()