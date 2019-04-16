import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        lbl_red = QLabel('Red')
        lbl_red.setStyleSheet("color: red;"
                              "border-style: solid;"
                              "border-width: 2px;"
                              "border-color: #FA8072;"
                              "border-radius: 3px")

        lbl_green = QLabel('Green')
        lbl_green.setStyleSheet("color: green;"
                                "background-color: #7FFFD4")

        lbl_blue = QLabel('Blue')
        lbl_blue.setStyleSheet("color: blue;"
                               "background-color: #87CEFA;"
                               "border-style: dashed;"
                               "border-width: 3px;"
                               "border-color: #1E90FF")

        vbox = QVBoxLayout()
        vbox.addWidget(lbl_red)
        vbox.addWidget(lbl_green)
        vbox.addWidget(lbl_blue)

        self.setLayout(vbox)

        self.setWindowTitle('Styled Widgets')
        self.show()


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = MyWidget()
        self.setCentralWidget(widget)
        self.setGeometry(300, 300, 200, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
