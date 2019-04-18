import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QDoubleSpinBox, QSpinBox, QLabel


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
        self.sb.valueChanged.connect(self.value_changed1)

        self.label2 = QLabel('0')

        self.label3 = QLabel('QDoubleSpinBox')

        self.dsb = QDoubleSpinBox()
        self.dsb.setRange(0, 100)
        self.dsb.setSingleStep(0.5)
        self.dsb.setPrefix('$ ')
        self.dsb.setDecimals(1)
        self.dsb.valueChanged.connect(self.value_changed2)

        self.label4 = QLabel('$ 0.0')

        grid = QGridLayout()
        grid.addWidget(self.label1, 0, 0)
        grid.addWidget(self.sb, 1, 0)
        grid.addWidget(self.label2, 2, 0)
        grid.addWidget(self.label3, 0, 1)
        grid.addWidget(self.dsb, 1, 1)
        grid.addWidget(self.label4, 2, 1)
        self.setLayout(grid)

        self.setWindowTitle('QSpinBox')
        self.setGeometry(300, 300, 300, 100)
        self.show()

    def value_changed1(self):
        self.label2.setText(str(self.sb.value()))

    def value_changed2(self):
        self.label4.setText('$ ' + str(self.dsb.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
