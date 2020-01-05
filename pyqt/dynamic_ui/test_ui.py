from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout


class TestUI(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Test")
        self.le = QLineEdit()
        self.btn = QPushButton("click")

        self.init_ui()

    def init_ui(self):
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.label)
        hlayout.addWidget(self.le)

        vlayout = QVBoxLayout()
        vlayout.addLayout(hlayout)
        vlayout.addWidget(self.btn)

        self.setLayout(vlayout)
        self.show()
