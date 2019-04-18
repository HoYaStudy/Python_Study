import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QLabel


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.label1 = QLabel('QSpinBox')

        self.sb = QSpinBox()
        self.sb.setMinimum(-10)
        self.sb.setMaximum(30)
        # self.sb.setRange(-10, 30)
        self.sb.setSingleStep(2)
        self.sb.valueChanged.connect(self.value_changed)

        self.label2 = QLabel('0')

        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.sb)
        vbox.addWidget(self.label2)
        vbox.addStretch()
        self.setLayout(vbox)

        self.setWindowTitle('QSpinBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def value_changed(self):
        self.label2.setText(str(self.sb.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
