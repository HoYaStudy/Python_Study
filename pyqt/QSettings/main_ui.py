import sys
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QTabWidget, QVBoxLayout
from sub_ui import SubUI


class MainUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.settings = QSettings("OrganizationName", "ApplicationName")

        self.init_ui()
        self.load_settings()

    def init_ui(self):
        tabs = QTabWidget()
        tabs.addTab(SubUI(), "SubUI")

        vlayout = QVBoxLayout()
        vlayout.addWidget(tabs)

        central_widget = QWidget()
        central_widget.setLayout(vlayout)
        self.setCentralWidget(central_widget)

        self.setWindowTitle("MainUI")
        self.show()

    def closeEvent(self, event):
        for widget in self.findChildren(QWidget) + [self]:
            if hasattr(widget, "save_settings") and callable(widget.save_settings):
                widget.save_settings()
        super().closeEvent(event)

    def save_settings(self):
        self.settings.setValue("geometry", self.saveGeometry())

    def load_settings(self):
        if self.settings.contains("geometry"):
            self.restoreGeometry(self.settings.value("geometry"))
        else:
            self.setGeometry(100, 100, 300, 300)


if __name__ == "__main__":
    APP = QApplication(sys.argv)
    ex = MainUI()
    sys.exit(APP.exec_())
