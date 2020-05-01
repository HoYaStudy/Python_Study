from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit


class SubUI(QWidget):
    def __init__(self):
        super().__init__()

        self.settings = QSettings("OrganizationName", "ApplicationName")

        self.label = QLabel("Input to save text")
        self.le = QLineEdit()
        self.init_ui()
        self.load_settings()

    def __del__(self):
        self.save_settings()

    def init_ui(self):
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.label)
        hlayout.addWidget(self.le)
        self.setLayout(hlayout)

    def save_settings(self):
        self.settings.setValue("label", self.le.text())

    def load_settings(self):
        if self.settings.contains("label"):
            self.le.setText(self.settings.value("label"))
