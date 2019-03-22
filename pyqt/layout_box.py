import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        label1 = QLabel('Label1', self)
        label2 = QLabel('Label2', self)

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(label1)
        hbox1.addWidget(label2)
        hbox1.addStretch(1)

        okButton = QPushButton('Button1')
        cancelButton = QPushButton('Button2')

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(okButton)
        hbox2.addWidget(cancelButton)
        hbox2.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addStretch(1)

        self.setLayout(vbox)
        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
