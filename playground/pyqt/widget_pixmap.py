import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        pixmap = QPixmap('landscape.jpg')
        image_label = QLabel()
        image_label.setPixmap(pixmap)
        image_size_label = QLabel('Width: ' + str(pixmap.width()) + ', Height: ' + str(pixmap.height()))
        image_size_label.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(image_label)
        vbox.addWidget(image_size_label)
        self.setLayout(vbox)

        self.setWindowTitle('QPixmap')
        self.move(300, 300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
