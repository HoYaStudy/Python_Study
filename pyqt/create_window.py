import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("My First Application")
        self.setWindowIcon(QIcon('terminal.png'))
        # self.move(300, 300)
        # self.resize(400, 200)
        self.setGeometry(300, 300, 400, 200)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
