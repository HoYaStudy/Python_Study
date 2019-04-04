import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QInputDialog, QPushButton, QLineEdit
from PyQt5.QtWidgets import QColorDialog, QFrame
from PyQt5.QtWidgets import QFontDialog, QLabel, QSizePolicy
from PyQt5.QtWidgets import QFileDialog, QTextEdit
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QColor


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.btn1 = QPushButton('Input Dialog', self)
        self.btn1.move(10, 10)
        self.btn1.clicked.connect(self.showInputDialog)

        self.le = QLineEdit(self)
        self.le.move(150, 14)

        color = QColor(0, 0, 0)

        self.btn2 = QPushButton('Color Dialog', self)
        self.btn2.move(10, 50)
        self.btn2.clicked.connect(self.showColorDialog)

        self.frm = QFrame(self)
        self.frm.setGeometry(150, 53, 100, 100)
        self.frm.setStyleSheet('QWidget { background-color: %s }' % color.name())

        btn3 = QPushButton('Font Dialog', self)
        btn3.move(10, 160)
        btn3.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        btn3.clicked.connect(self.showFontDialog)

        self.lbl = QLabel('Lorem ipsum dolor sit amet', self)
        self.lbl.move(150, 166)

        btn4 = QPushButton('File Dialog', self)
        btn4.move(10, 200)
        btn4.clicked.connect(self.showFileDialog)

        self.te = QTextEdit(self)
        self.te.setGeometry(150, 205, 150, 150)

        self.setWindowTitle('Dialog')
        self.setGeometry(300, 300, 330, 380)
        self.show()

    def showInputDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        if ok:
            self.le.setText(str(text))

    def showColorDialog(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.frm.setStyleSheet('QWidget { background-color: %s }' % color.name())

    def showFontDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)

    def showFileDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')
        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.te.setText(data)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())