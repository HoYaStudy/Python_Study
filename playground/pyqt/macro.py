import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, \
                            QFileDialog, \
                            QLineEdit, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
import win32api, win32con, pyautogui

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.open_btn = QPushButton('Open Image')
        self.open_btn.clicked.connect(self.show_dialog)

        self.label = []

        self.x_le = QLineEdit()
        self.y_le = QLineEdit()
        self.n_le = QLineEdit()
        self.t_le = QLineEdit()

        self.click_btn = QPushButton('Click')
        self.click_btn.clicked.connect(self.click_btn_click)

        self.start_btn = QPushButton('Start', self)
        self.start_btn.clicked.connect(self.start_btn_click)

        self.timer = QTimer()

        self.fname = []

        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout()

        self.initUI()

    def initUI(self):
        hbox_xy = QHBoxLayout()
        hbox_xy.addWidget(QLabel('Position X: '))
        hbox_xy.addWidget(self.x_le)
        hbox_xy.addWidget(QLabel('Position Y: '))
        hbox_xy.addWidget(self.y_le)

        hbox_nt = QHBoxLayout()
        hbox_nt.addWidget(QLabel('Count: '))
        hbox_nt.addWidget(self.n_le)
        hbox_nt.addWidget(QLabel('Delay: '))
        hbox_nt.addWidget(self.t_le)

        self.vbox.addWidget(self.open_btn)
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.hbox)
        self.vbox.addStretch(1)
        self.vbox.addLayout(hbox_xy)
        self.vbox.addLayout(hbox_nt)
        self.vbox.addWidget(self.click_btn)
        self.vbox.addWidget(self.start_btn)

        self.setLayout(self.vbox)

        self.setWindowTitle('PyQt5 Macro')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def show_dialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')
        if fname[0]:
            pixmap = QPixmap(fname[0])
            self.label.append(QLabel())
            self.label[-1].setPixmap(pixmap.scaledToWidth(pixmap.width() * 1.1))
            self.fname.append(fname[0])
            self.hbox.addWidget(self.label[-1])

    def start_btn_click(self):
        delay = int(self.t_le.text())
        self.timer.start(delay * 1000)
        self.timer.timeout.connect(self.mouse_click)

    def click_btn_click(self):
        n = int(self.n_le.text())
        t = float(self.t_le.text())
        if self.x_le.text() and self.y_le.text():
            x_pos = int(self.x_le.text())
            y_pos = int(self.y_le.text())
            pyautogui.click(x_pos, y_pos, clicks=n, interval=t)
        elif len(self.fname):
            for i in range(n):
                for j in range(len(self.fname)):
                    center = pyautogui.locateCenterOnScreen(self.fname[j])
                    pyautogui.click(center, interval=t)

    def mouse_click(self):
        x = int(self.x_le.text())
        y = int(self.y_le.text())

        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
