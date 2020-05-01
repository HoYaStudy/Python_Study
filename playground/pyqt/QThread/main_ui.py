import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtWidgets import QProgressBar, QPushButton
from worker import Worker


class MainUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.worker = Worker()
        self.worker.start()

        self.prog_bar = QProgressBar()
        self.btn = QPushButton("Pause")

        self.init_ui()

    def init_ui(self):
        self.worker.changed_value.connect(self.prog_bar.setValue)
        self.btn.clicked.connect(self.click_button)

        vlayout = QVBoxLayout()
        vlayout.addWidget(self.prog_bar)
        vlayout.addWidget(self.btn)

        central_widget = QWidget()
        central_widget.setLayout(vlayout)
        self.setCentralWidget(central_widget)

        self.setWindowTitle("MainUI")
        self.show()

    @pyqtSlot()
    def click_button(self):
        self.worker.toggle_status()
        self.btn.setText({True: "Pause", False: "Resume"}[self.worker.get_status])


if __name__ == "__main__":
    APP = QApplication(sys.argv)
    ex = MainUI()
    sys.exit(APP.exec_())
