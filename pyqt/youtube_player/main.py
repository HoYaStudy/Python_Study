import sys
import datetime
import re
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, pyqtSignal
# from PyQt5 import uic

from lib.YouViewerLayout import Ui_MainWindow
from lib.AuthDialog import AuthDialog

# Form = uic.loadUiType('./ui/you_viewer_v1.0.ui')[0]

# class Main(QMainWindow, Form):
class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.user_id = None
        self.user_pw = None

        self.setupUi(self)
        self.initAuth()
        self.initSignal()

    def initAuth(self):
        self.previewBtn.setEnabled(False)
        self.fileNavBtn.setEnabled(False)
        self.qualityCB.setEnabled(False)
        self.startBtn.setEnabled(False)
        self.calendarWidget.setEnabled(False)
        self.urlLE.setEnabled(False)
        self.pathLE.setEnabled(False)
        self.showStatusMsg('Not Authenticated')

    def activateAuth(self):
        self.previewBtn.setEnabled(True)
        self.fileNavBtn.setEnabled(True)
        self.qualityCB.setEnabled(True)
        self.calendarWidget.setEnabled(True)
        self.urlLE.setEnabled(True)
        self.pathLE.setEnabled(True)
        self.showStatusMsg('Authenticated')

    def showStatusMsg(self, msg):
        self.statusbar.showMessage(msg)

    def initSignal(self):
        self.loginBtn.clicked.connect(self.checkAuth)

    @pyqtSlot()
    def checkAuth(self):
        dialog = AuthDialog()
        dialog.exec_()
        self.user_id = dialog.user_id
        self.user_pw = dialog.user_pw

        if True:
            self.activateAuth()
            self.loginBtn.setText('Authentication Succeed')
            self.loginBtn.setEnabled(False)
            self.urlLE.setFocus(True)
        else:
            QMessageBox.about(self, 'Failed to authenticate', 'Wrong ID or password')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    you_viewer_main = Main()
    you_viewer_main.show()
    app.exec_()
