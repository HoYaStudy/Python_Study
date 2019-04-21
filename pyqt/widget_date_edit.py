import sys
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QDateEdit, QLabel


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        label = QLabel('QDateEdit')

        date_edit = QDateEdit(self)
        date_edit.setDate(QDate.currentDate())
        date_edit.setMinimumDate(QDate(1900, 1, 1))
        date_edit.setMaximumDate(QDate(2100, 12, 31))
        # date_edit.setDateRange(QDate(1900, 1, 1), QDate(2100, 12, 31))

        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addWidget(date_edit)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('QDateEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
