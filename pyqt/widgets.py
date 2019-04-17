import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout
from PyQt5.QtWidgets import QLabel, QCheckBox, QPushButton, QRadioButton, QComboBox, QLineEdit
from PyQt5.QtWidgets import QProgressBar, QSlider, QDial, QFrame, QSplitter
from PyQt5.QtCore import Qt, QBasicTimer


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # QLabel
        label1 = QLabel('Label1', self)
        label1.setAlignment(Qt.AlignCenter)
        font1 = label1.font()
        font1.setPointSize(15)
        label1.setFont(font1)

        label2 = QLabel('Label2', self)
        label2.setAlignment(Qt.AlignVCenter)
        font2 = label2.font()
        font2.setFamily('Consolas')
        font2.setBold(True)
        label2.setFont(font2)

        label3 = QLabel('Label3', self)
        label3.setAlignment(Qt.AlignHCenter)
        font3 = label3.font()
        font3.setPointSize(8)
        label3.setFont(font3)

        # QCheckBox
        checkbox1 = QCheckBox('CheckBox1', self)
        checkbox1.toggle()
        checkbox1.stateChanged.connect(self.changeTitle)

        checkbox2 = QCheckBox('CheckBox2', self)
        checkbox2.setTristate()

        checkbox3 = QCheckBox(self)
        checkbox3.setText('CheckBox3');

        # QPushButton
        btn1 = QPushButton('&Button1', self)
        btn1.setCheckable(True)
        btn1.toggle()

        btn2 = QPushButton(self)
        btn2.setText('&Button2')

        btn3 = QPushButton('&Button3', self)
        btn3.setEnabled(False)

        # QRadioButton
        rbtn1 = QRadioButton('RadioButton1', self)
        rbtn1.setChecked(True)

        rbtn2 = QRadioButton(self)
        rbtn2.setText('RadioButton2')

        # QComboBox
        cb = QComboBox(self)
        cb.addItem('Combo1')
        cb.addItem('Combo2')
        cb.addItem('Combo3')
        cb.addItem('Combo4')
        cb.activated[str].connect(self.onActivated)

        self.label4 = QLabel('Label4', self)

        # QLineEdit
        le = QLineEdit(self)
        le.textChanged[str].connect(self.onChanged)

        self.label5 = QLabel('Label5', self)

        # QProgressBar
        self.pbar1 = QProgressBar(self)

        pbar2 = QProgressBar(self)
        pbar2.setMaximum(0)
        pbar2.setMinimum(0)

        self.btn4 = QPushButton('Start', self)
        self.btn4.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0

        # QSlider & QDial
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setRange(0, 50)
        self.slider.setSingleStep(2)

        self.dial = QDial(self)
        self.dial.setRange(0, 50)

        self.slider.valueChanged.connect(self.dial.setValue)
        self.dial.valueChanged.connect(self.slider.setValue)

        btn5 = QPushButton('Default', self)
        btn5.clicked.connect(self.button_clicked)

        # QSplitter (QFrame)
        top = QFrame()
        top.setFrameShape(QFrame.Box)

        midleft = QFrame()
        midleft.setFrameShape(QFrame.StyledPanel)

        midright = QFrame()
        midright.setFrameShape(QFrame.Panel)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.WinPanel)
        bottom.setFrameShadow(QFrame.Sunken)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(midleft)
        splitter1.addWidget(midright)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(top)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        # Layout
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 1, 0)
        grid.addWidget(label3, 2, 0)

        grid.addWidget(checkbox1, 0, 1)
        grid.addWidget(checkbox2, 1, 1)
        grid.addWidget(checkbox3, 2, 1)

        grid.addWidget(btn1, 0, 2)
        grid.addWidget(btn2, 1, 2)
        grid.addWidget(btn3, 2, 2)

        grid.addWidget(rbtn1, 3, 0)
        grid.addWidget(rbtn2, 3, 1)

        grid.addWidget(cb, 4, 0)
        grid.addWidget(self.label4, 4, 1)

        grid.addWidget(le, 5, 0)
        grid.addWidget(self.label5, 5, 1)

        grid.addWidget(self.btn4, 6, 0)
        grid.addWidget(self.pbar1, 6, 1)
        grid.addWidget(pbar2, 6, 2)

        grid.addWidget(btn5, 7, 0)
        grid.addWidget(self.slider, 7, 1)
        grid.addWidget(self.dial, 7, 2)

        grid.addWidget(splitter2, 8, 0)

        self.setWindowTitle('Widgets')
        self.setGeometry(300, 300, 300, 500)
        self.show()

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')

    def onActivated(self, text):
        self.label4.setText(text)
        self.label4.adjustSize()

    def onChanged(self, text):
        self.label5.setText(text)
        self.label5.adjustSize()

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn4.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn4.setText('Stop')

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn4.setText('Finished')
            return
        self.step = self.step + 1
        self.pbar1.setValue(self.step)

    def button_clicked(self):
        self.slider.setValue(0)
        self.dial.setValue(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
