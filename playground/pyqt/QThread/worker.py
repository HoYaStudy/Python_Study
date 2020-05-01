from PyQt5.QtCore import QThread, QWaitCondition, QMutex, pyqtSignal
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit


class Worker(QThread):
    changed_value = pyqtSignal(int)

    def __init__(self):
        super().__init__()

        self._status = True

        self.cond = QWaitCondition()
        self.mutex = QMutex()
        self.cnt = 0

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            self.mutex.lock()

            if not self._status:
                self.cond.wait(self.mutex)

            if 100 == self.cnt:
                self.cnt = 0
            self.cnt += 1
            self.changed_value.emit(self.cnt)
            self.msleep(100)

            self.mutex.unlock()

    def toggle_status(self):
        self._status = not self._status
        if self._status:
            self.cond.wakeAll()

    @property
    def get_status(self):
        return self._status
