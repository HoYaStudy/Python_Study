import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QDialog,  \
                            QTabWidget, QLabel, QLineEdit, QGroupBox, QComboBox, QCheckBox, \
                            QDialogButtonBox, QTextBrowser


class MyApp(QDialog):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        tabs = QTabWidget()
        tabs.addTab(Tab1(), 'Tab1')
        tabs.addTab(Tab2(), 'Tab2')
        tabs.addTab(Tab3(), 'Tab3')

        dialog_btn_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        dialog_btn_box.accepted.connect(self.accept)
        dialog_btn_box.rejected.connect(self.reject)

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)
        vbox.addWidget(dialog_btn_box)

        self.setLayout(vbox)

        self.setWindowTitle('QTabWidget')
        self.setGeometry(300, 300, 300, 200)
        self.show()


class Tab1(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        name = QLabel('Name:')
        name_le = QLineEdit()
        age = QLabel('Age:')
        age_le = QLineEdit()
        nation = QLabel('Nation:')
        nation_le = QLineEdit()

        vbox = QVBoxLayout()
        vbox.addWidget(name)
        vbox.addWidget(name_le)
        vbox.addWidget(age)
        vbox.addWidget(age_le)
        vbox.addWidget(nation)
        vbox.addWidget(nation_le)
        vbox.addStretch()

        self.setLayout(vbox)


class Tab2(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        lang_list = ['Korean', 'English', 'Chinese']
        combo = QComboBox()
        combo.addItems(lang_list)

        lang_group = QGroupBox('Select Your Language')
        vbox1 = QVBoxLayout()
        vbox1.addWidget(combo)
        lang_group.setLayout(vbox1)

        korean_cb = QCheckBox('Korean')
        english_cb = QCheckBox('English')
        chinese_cb = QCheckBox('Chinese')

        learn_group = QGroupBox('Select What You Want To Learn')
        vbox2 = QVBoxLayout()
        vbox2.addWidget(korean_cb)
        vbox2.addWidget(english_cb)
        vbox2.addWidget(chinese_cb)
        learn_group.setLayout(vbox2)

        vbox = QVBoxLayout()
        vbox.addWidget(lang_group)
        vbox.addWidget(learn_group)

        self.setLayout(vbox)


class Tab3(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        label = QLabel('Terms and Conditions')
        tb = QTextBrowser()
        tb.setText('This is the terms and conditions')
        cb = QCheckBox('Check the terms and conditions')

        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addWidget(tb)
        vbox.addWidget(cb)

        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
