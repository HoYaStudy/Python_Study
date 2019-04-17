import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QVBoxLayout, QGroupBox
from PyQt5.QtWidgets import QRadioButton, QCheckBox, QPushButton, QMenu


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.addWidget(self.createExclusiveGroup1(), 0, 0)
        grid.addWidget(self.createExclusiveGroup2(), 1, 0)
        grid.addWidget(self.createNonExclusiveGroup(), 0, 1)
        grid.addWidget(self.createPushButtonGroup(), 1, 1)

        self.setLayout(grid)

        self.setWindowTitle('QGroupBox')
        self.setGeometry(300, 300, 480, 320)
        self.show()

    def createExclusiveGroup1(self):
        radio1 = QRadioButton('Radio1')
        radio2 = QRadioButton('Radio2')
        radio3 = QRadioButton('Radio3')
        radio1.setChecked(True)

        group_box = QGroupBox('Group 1')
        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        group_box.setLayout(vbox)

        return group_box

    def createExclusiveGroup2(self):
        radio1 = QRadioButton('Radio1')
        radio2 = QRadioButton('Radio2')
        radio3 = QRadioButton('Radio3')
        radio1.setChecked(True)

        cb = QCheckBox('CheckBox')
        cb.setChecked(True)

        group_box = QGroupBox('Group 2')
        group_box.setCheckable(True)
        group_box.setChecked(True)
        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        vbox.addWidget(cb)
        vbox.addStretch(1)
        group_box.setLayout(vbox)

        return group_box

    def createNonExclusiveGroup(self):
        cb1 = QCheckBox('CheckBox 1')
        cb2 = QCheckBox('CheckBox 2')
        cb2.setChecked(True)
        cb3 = QCheckBox('CheckBox 3')
        cb3.setTristate(True)

        group_box = QGroupBox('Group 3')
        group_box.setFlat(True)
        vbox = QVBoxLayout()
        vbox.addWidget(cb1)
        vbox.addWidget(cb2)
        vbox.addWidget(cb3)
        vbox.addStretch(1)
        group_box.setLayout(vbox)

        return group_box

    def createPushButtonGroup(self):
        pb1 = QPushButton('Normal Button')
        pb2 = QPushButton('Toggle Button')
        pb2.setCheckable(True)
        pb2.setChecked(True)
        pb3 = QPushButton('Flat Button')
        pb3.setFlat(True)
        pb4 = QPushButton('Popup Button')
        menu = QMenu(self)
        menu.addAction('First Item')
        menu.addAction('Second Item')
        menu.addAction('Third Item')
        menu.addAction('Fourth Item')
        pb4.setMenu(menu)

        group_box = QGroupBox('Group 4')
        group_box.setCheckable(True)
        group_box.setChecked(True)
        vbox = QVBoxLayout()
        vbox.addWidget(pb1)
        vbox.addWidget(pb2)
        vbox.addWidget(pb3)
        vbox.addWidget(pb4)
        vbox.addStretch(1)
        group_box.setLayout(vbox)

        return group_box


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())