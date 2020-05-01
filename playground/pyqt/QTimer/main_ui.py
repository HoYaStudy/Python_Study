import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QPushButton


class MainUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self._time = 0
        self._state = True
        self._single_mode = False

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.inc_time)
        self.timer.start()

        self.label1 = QLabel()
        self.label2 = QLabel()
        self.btn1 = QPushButton("Pause")
        self.btn2 = QPushButton("Single Shot On")
        self.btn3 = QPushButton("Single Shot")

        self.init_ui()

    def init_ui(self):
        self.btn1.clicked.connect(self.click_button1)
        self.btn2.clicked.connect(self.click_button2)
        self.btn3.clicked.connect(self.click_button3)

        hlayout1 = QHBoxLayout()
        hlayout1.addWidget(self.label1)
        hlayout1.addWidget(self.label2)

        hlayout2 = QHBoxLayout()
        hlayout2.addWidget(self.btn1)
        hlayout2.addWidget(self.btn2)
        hlayout2.addWidget(self.btn3)

        vlayout = QVBoxLayout()
        vlayout.addLayout(hlayout1)
        vlayout.addLayout(hlayout2)

        central_widget = QWidget()
        central_widget.setLayout(vlayout)
        self.setCentralWidget(central_widget)

        self.setWindowTitle("MainUI")
        self.show()

    def inc_time(self):
        self._time += 1
        self.label1.setText(str(self._time))

    def click_button1(self):
        self._state = not self._state
        if self._state:
            self.btn1.setText("Resume")
            self.timer.stop()
        else:
            self.btn1.setText("Pause")
            self.timer.start()

    def click_button2(self):
        self._single_mode = not self._single_mode
        self.btn1.setText("Resume")
        self.timer.setSingleShot(self._single_mode)
        if self._single_mode:
            self.btn2.setText("Single Shot Off")
        else:
            self.btn2.setText("Single Shot On")

    def click_button3(self):
        self.label2.setText("Start")
        self.timer.singleShot(1000, self.print_text)

    def print_text(self):
        self.label2.setText("End")

if __name__ == "__main__":
    APP = QApplication(sys.argv)
    ex = MainUI()
    sys.exit(APP.exec_())
