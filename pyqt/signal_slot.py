import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, \
                            QDial, QLCDNumber, QPushButton, QLabel


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)

        dial = QDial(self)
        dial.valueChanged.connect(lcd.display)

        x = 0
        y = 0
        self.text = 'x : {0}, y: {1}'.format(x, y)
        self.label = QLabel(self.text, self)
        self.label.move(20, 20)

        btn1 = QPushButton('Big', self)
        btn1.clicked.connect(self.resizeBig)

        btn2 = QPushButton('Small', self)
        btn2.clicked.connect(self.resizeSmall)

        self.setMouseTracking(True)

        # Layout
        hbox = QHBoxLayout()
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(dial)
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.setWindowTitle('Signal and Slot')
        self.setGeometry(300, 300, 250, 250)
        self.show()

    def resizeBig(self):
        self.resize(500, 500)

    def resizeSmall(self):
        self.resize(250, 250)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_F:
            self.showFullScreen()
        elif e.key() == Qt.Key_N:
            self.showNormal()

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()

        self.text = 'x: {0}, y: {1}'.format(x, y)
        self.label.setText(self.text)
        self.label.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
