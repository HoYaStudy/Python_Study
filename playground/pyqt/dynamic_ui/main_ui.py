import sys
import PyQt5
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QScrollArea,
)
from test_ui import TestUI


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.add_btn = QPushButton("Add")
        self.add_btn.clicked.connect(self.click_add_btn)

        self.remove_btn = QPushButton("Remove")
        self.remove_btn.clicked.connect(self.click_remove_btn)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.init_ui()

    def init_ui(self):
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.add_btn)
        self.main_layout.addWidget(self.remove_btn)
        self.main_layout.addWidget(TestUI())
        self.centralWidget = QWidget()
        self.centralWidget.setLayout(self.main_layout)
        self.setCentralWidget(self.centralWidget)
        self.show()

    def click_add_btn(self):
        self.main_layout.addWidget(TestUI())
        self.setFixedSize(
            self.main_layout.sizeHint()
            + PyQt5.QtCore.QSize(0, TestUI().frameGeometry().height())
        )

    def click_remove_btn(self):
        if self.main_layout.count() > 3:
            child = self.main_layout.takeAt(self.main_layout.count() - 1)
            child.widget().deleteLater()
            print(self.main_layout.count())
            print(self.main_layout.sizeHint())
            self.setFixedSize(self.main_layout.sizeHint())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
