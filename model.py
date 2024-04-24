from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget


class Model(QWidget):
    observers = QtCore.pyqtSignal()

    def __init__(self, value=0):
        super().__init__()
        self.value = 0

    def set_value(self, value):
        self.value = value
        self.observers.emit()

    def get_value(self):
        return self.value
