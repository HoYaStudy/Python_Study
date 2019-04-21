import sys
from PyQt5.QtCore import QTime
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTimeEdit, QLabel


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        label = QLabel('QTimeEdit')

        time_edit = QTimeEdit(self)
        time_edit.setTime(QTime.currentTime())
        time_edit.setTimeRange(QTime(3, 00, 00), QTime(23, 30, 00))
        time_edit.setDisplayFormat('hh:mm:ss')

        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addWidget(time_edit)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('QTimeEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
