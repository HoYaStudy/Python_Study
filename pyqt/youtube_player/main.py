import sys
import datetime
import re
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QUrl
# from PyQt5 import uic
import pytube

from lib.YouViewerLayout import Ui_MainWindow
from lib.AuthDialog import AuthDialog

# Form = uic.loadUiType('./ui/you_viewer_v1.0.ui')[0]

# class Main(QMainWindow, Form):
class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.user_id = None
        self.user_pw = None
        self.is_playing = False
        self.youtube = None
        self.youtube_fsize = 0

        self.setupUi(self)
        self.initAuth()
        self.initSignal()

    def initAuth(self):
        self.previewBtn.setEnabled(False)
        self.fileNavBtn.setEnabled(False)
        self.qualityCB.setEnabled(False)
        self.downloadBtn.setEnabled(False)
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
            self.appendLogMsg('Successfully login')
        else:
            QMessageBox.about(self, 'Failed to authenticate', 'Wrong ID or password')

    def initSignal(self):
        self.loginBtn.clicked.connect(self.checkAuth)
        self.previewBtn.clicked.connect(self.loadUrl)
        self.endBtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.webView.loadProgress.connect(self.showProgressBrowserLoading)
        self.fileNavBtn.clicked.connect(self.selectDownPath)
        self.calendarWidget.clicked.connect(self.logCalender)
        self.downloadBtn.clicked.connect(self.downloadYoutube)

    def loadUrl(self):
        url = self.urlLE.text().strip()
        v = re.compile('^https://www.youtube.com/?')
        if self.is_playing:
            self.appendLogMsg('Clicked Stop button')
            self.webView.load(QUrl('about:blank'))
            self.previewBtn.setText('Play')
            self.is_playing = False
            self.urlLE.clear()
            self.urlLE.setFocus(True)
            self.downloadBtn.setEnabled(False)
            self.qualityCB.clear()
            self.progressBar_2.setValue(0)
            self.showStatusMsg('Authenticated')
        else:
            if v.match(url) is not None:
                self.appendLogMsg('Clicked Play button')
                self.webView.load(QUrl(url))
                self.showStatusMsg(url + ' is playing')
                self.previewBtn.setText('Stop')
                self.is_playing = True
                self.downloadBtn.setEnabled(True)
                self.initYoutube(url)
            else:
                QMessageBox.about(self, 'Not available URL', 'It is not a youtube URL.')
                self.urlLE.clear()
                self.urlLE.setFocus(True)

    def initYoutube(self, url):
        video_list = pytube.YouTube(url)
        video_list.register_on_progress_callback(self.showProgressDownloadLoading)
        self.youtube = video_list.streams.all()
        self.qualityCB.clear()
        for q in self.youtube:
            temp_list, str_list = [], []
            temp_list.append(str(q.mime_type or ''))
            temp_list.append(str(q.res or ''))
            temp_list.append(str(q.fps or ''))
            temp_list.append(str(q.abr or ''))
            str_list = [x for x in temp_list if x != '']
            self.qualityCB.addItem(', '.join(str_list))

    @pyqtSlot()
    def downloadYoutube(self):
        down_path = self.pathLE.text().strip()
        if down_path is None or down_path == '' or not down_path:
            QMessageBox.about(self, 'Select Path', 'Select path to download')
            return None

        self.youtube_fsize = self.youtube[self.qualityCB.currentIndex()].filesize
        self.youtube[self.qualityCB.currentIndex()].download(down_path)
        self.appendLogMsg('Clicked Download button')

    @pyqtSlot()
    def selectDownPath(self):
        fpath = QFileDialog.getExistingDirectory(self, 'Select Directory')
        self.pathLE.setText(fpath)

    @pyqtSlot()
    def logCalender(self):
        cur_date = self.calendarWidget.selectedDate()
        self.appendLogMsg('Clicked calendar : ' + str(cur_date.year()) + '-' + str(cur_date.month()) + '-' + str(cur_date.day()))

    @pyqtSlot(int)
    def showProgressBrowserLoading(self, v):
        self.progressBar.setValue(v)

    @pyqtSlot(int)
    def showProgressDownloadLoading(self, stream, chunk, file_handler, bytes_remaining):
        self.progressBar_2.setValue(int(((self.youtube_fsize - bytes_remaining) / self.youtube_fsize) * 100))

    def showStatusMsg(self, msg):
        self.statusbar.showMessage(msg)

    def appendLogMsg(self, act):
        now = datetime.datetime.now()
        nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
        msg =  '[' + nowDatetime + '] ' + self.user_id + ' : ' + act
        self.logPTE.appendPlainText(msg)

        with open('./log.txt', 'a') as f:
            f.write(msg + '\n')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    you_viewer_main = Main()
    you_viewer_main.show()
    app.exec_()
