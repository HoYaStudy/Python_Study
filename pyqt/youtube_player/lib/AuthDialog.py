import sys
from PyQt5.QtWidgets import *


class AuthDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.user_id = None
        self.user_pw = None

        self.setupUI()

    def setupUI(self):
        idLabel = QLabel('ID: ')
        pwLabel = QLabel('PW: ')
        self.idLE = QLineEdit()
        self.pwLE = QLineEdit()
        self.pwLE.setEchoMode(QLineEdit().Password)
        self.btn = QPushButton('Login')
        self.btn.clicked.connect(self.submitLogin)

        layout = QGridLayout()
        layout.addWidget(idLabel, 0, 0)
        layout.addWidget(self.idLE, 0, 1)
        layout.addWidget(self.btn, 0, 2)
        layout.addWidget(pwLabel, 1, 0)
        layout.addWidget(self.pwLE, 1, 1)
        self.setLayout(layout)

        # self.setGeometry(300, 1800, 300, 100)
        self.setWindowTitle('Sign In')
        self.setFixedSize(300, 100)

    def submitLogin(self):
        self.user_id = self.idLE.text()
        if self.user_id is None or self.user_id == '' or not self.user_id:
            QMessageBox.about(self, 'Error: Login', 'Please, input your ID')
            self.idLE.setFocus(True)
            return None

        self.user_pw = self.pwLE.text()
        if self.user_pw is None or self.user_pw == '' or not self.user_pw:
            QMessageBox.about(self, 'Error: Login', 'Please, input your password')
            self.pwLE.setFocus(True)
            return None

        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    loginDialog = AuthDialog()
    loginDialog.show()
    app.exec_()
