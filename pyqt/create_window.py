import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDesktopWidget, QPushButton, QToolTip, QAction, qApp
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QFont


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("My First Application")
        self.setWindowIcon(QIcon('terminal.png'))
        # self.move(300, 300)
        self.resize(400, 200)
        # self.setGeometry(300, 400, 400, 200)
        self.moveCenter()

        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        QToolTip.setFont(QFont('Consolas', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        btn = QPushButton('Quit', self)
        btn.move(50, 100)
        btn.resize(btn.sizeHint())
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.statusBar().showMessage('Ready')

        self.show()

    def moveCenter(self):
        fg = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        fg.moveCenter(cp)
        self.move(fg.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
