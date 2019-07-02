import sys
import datetime
import re
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import uic

from lib.YouViewerLayout import Ui_MainWindow

# Form = uic.loadUiType('./ui/you_viewer_v1.0.ui')[0]

# class Main(QMainWindow, Form):
class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    you_viewer_main = Main()
    you_viewer_main.show()
    app.exec_()
