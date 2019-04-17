import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QGroupBox
from PyQt5.QtWidgets import QLabel, QCheckBox, QPushButton, QRadioButton, QComboBox, QLineEdit
from PyQt5.QtWidgets import QProgressBar, QSlider, QDial, QFrame, QSplitter
from PyQt5.QtCore import Qt, QBasicTimer
from PyQt5.QtGui import QIntValidator, QDoubleValidator


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Echo Group
        self.echo_group = QGroupBox('Echo')

        self.echo_le1 = QLineEdit()
        self.echo_le1.setPlaceholderText('Normal')
        self.echo_le1.setEchoMode(QLineEdit.Normal)
        self.echo_le1.setFocus()

        self.echo_le2 = QLineEdit()
        self.echo_le2.setPlaceholderText('NoEcho')
        self.echo_le2.setEchoMode(QLineEdit.NoEcho)

        self.echo_le3 = QLineEdit()
        self.echo_le3.setPlaceholderText('Password')
        self.echo_le3.setEchoMode(QLineEdit.Password)

        self.echo_le4 = QLineEdit()
        self.echo_le4.setPlaceholderText('PasswordEchoOnEdit')
        self.echo_le4.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.echo_layout = QGridLayout()
        self.echo_layout.addWidget(self.echo_le1, 0, 0)
        self.echo_layout.addWidget(self.echo_le2, 1, 0)
        self.echo_layout.addWidget(self.echo_le3, 2, 0)
        self.echo_layout.addWidget(self.echo_le4, 3, 0)
        self.echo_group.setLayout(self.echo_layout)

        # Validator Group
        self.validator_group = QGroupBox('Validator')

        self.validator_le1 = QLineEdit()
        self.validator_le1.setPlaceholderText('None')
        self.validator_le1.setValidator(None)

        self.validator_le2 = QLineEdit()
        self.validator_le2.setPlaceholderText('QIntValidator')
        self.validator_le2.setValidator(QIntValidator(-99, 99))

        double_validator = QDoubleValidator(-999.0, 999.0, 2)
        double_validator.setNotation(QDoubleValidator.StandardNotation)
        self.validator_le3 = QLineEdit()
        self.validator_le3.setPlaceholderText('QIntValidator')
        self.validator_le3.setValidator(double_validator)

        self.validator_layout = QGridLayout()
        self.validator_layout.addWidget(self.validator_le1, 0, 0)
        self.validator_layout.addWidget(self.validator_le2, 1, 0)
        self.validator_layout.addWidget(self.validator_le3, 2, 0)
        self.validator_group.setLayout(self.validator_layout)

        # Alignment Group
        self.alignment_group = QGroupBox('Alignment')

        self.alignment_le1 = QLineEdit()
        self.alignment_le1.setPlaceholderText('AlignLeft')
        self.alignment_le1.setAlignment(Qt.AlignLeft)

        self.alignment_le2 = QLineEdit()
        self.alignment_le2.setPlaceholderText('AlignCenter')
        self.alignment_le2.setAlignment(Qt.AlignCenter)

        self.alignment_le3 = QLineEdit()
        self.alignment_le3.setPlaceholderText('AlignRight')
        self.alignment_le3.setAlignment(Qt.AlignRight)

        self.alignment_layout = QGridLayout()
        self.alignment_layout.addWidget(self.alignment_le1, 0, 0)
        self.alignment_layout.addWidget(self.alignment_le2, 1, 0)
        self.alignment_layout.addWidget(self.alignment_le3, 2, 0)
        self.alignment_group.setLayout(self.alignment_layout)

        # Input-Mask Group
        self.input_mask_group = QGroupBox('Input Mask')

        self.input_mask_le1 = QLineEdit()
        self.input_mask_le1.setInputMask('')

        self.input_mask_le2 = QLineEdit()
        self.input_mask_le2.setInputMask('000-0000-0000')

        self.input_mask_le3 = QLineEdit()
        self.input_mask_le3.setInputMask('0000-00-00')

        self.input_mask_le4 = QLineEdit()
        self.input_mask_le4.setInputMask('>AAAAA-AAAAA-AAAAA-AAAAA;#')

        self.input_mask_layout = QGridLayout()
        self.input_mask_layout.addWidget(self.input_mask_le1, 0, 0)
        self.input_mask_layout.addWidget(self.input_mask_le2, 1, 0)
        self.input_mask_layout.addWidget(self.input_mask_le3, 2, 0)
        self.input_mask_layout.addWidget(self.input_mask_le4, 3, 0)
        self.input_mask_group.setLayout(self.input_mask_layout)

        # Access Group
        self.access_group = QGroupBox('Access')

        self.access_le1 = QLineEdit()
        self.access_le1.setPlaceholderText('False')
        self.access_le1.setReadOnly(False)

        self.access_le2 = QLineEdit()
        self.access_le2.setPlaceholderText('True')
        self.access_le2.setReadOnly(True)

        self.access_layout = QGridLayout()
        self.access_layout.addWidget(self.access_le1, 0, 0)
        self.access_layout.addWidget(self.access_le2, 1, 0)
        self.access_group.setLayout(self.access_layout)

        # Clear Button
        btn = QPushButton('Clear', self)
        btn.move(50, 100)
        btn.clicked.connect(self.clearText)

        # Layout
        self.layout = QGridLayout()
        self.layout.addWidget(self.echo_group, 0, 0)
        self.layout.addWidget(self.validator_group, 0, 1)
        self.layout.addWidget(self.alignment_group, 1, 0)
        self.layout.addWidget(self.input_mask_group, 1, 1)
        self.layout.addWidget(self.access_group, 2, 0)
        self.layout.addWidget(btn, 3, 0)
        self.setLayout(self.layout)

        self.setWindowTitle('Widget: Line Edit')
        self.show()

    def clearText(self):
        self.echo_le1.clear()
        self.echo_le2.clear()
        self.echo_le3.clear()
        self.echo_le4.clear()

        self.validator_le1.clear()
        self.validator_le2.clear()
        self.validator_le3.clear()

        self.alignment_le1.clear()
        self.alignment_le2.clear()
        self.alignment_le3.clear()

        self.input_mask_le1.clear()
        self.input_mask_le2.clear()
        self.input_mask_le3.clear()
        self.input_mask_le4.clear()

        self.access_le1.clear()
        self.access_le2.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
