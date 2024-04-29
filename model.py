from typing import Literal
from PyQt5 import QtCore
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QWidget
from os.path import isfile


class Model(QWidget):
    observers = QtCore.pyqtSignal()
    log = QtCore.pyqtSignal(str)
    value_A = 0
    value_B = 0
    value_C = 0

    def __init__(self):
        super().__init__()

    def init_values(self):
        self.load_values()

    def load_values(self):
        if isfile("values.txt"):
            with open("values.txt", "r") as file:
                value_A, value_B, value_C = map(int, file.readlines())
                self.set_value(value_A, value_B, value_C)

    def save_values(self):
        with open("values.txt", "w") as file:
            file.write(f"{self.value_A}\n{self.value_B}\n{self.value_C}")

    def set_value(self, value_A: int | None = None, value_B: int | None = None, value_C: int | None = None):
        if value_A:
            self.value_A = value_A
            if self.value_A > self.value_B:
                self.value_B = self.value_A
            if self.value_C < self.value_B:
                self.value_C = self.value_B
        if value_C:
            self.value_C = value_C
            if self.value_C < self.value_B:
                self.value_B = self.value_C
            if self.value_A > self.value_B:
                self.value_A = self.value_B
        if value_B:
            if self.value_A <= value_B <= self.value_C:
                self.value_B = value_B
            else:
                self.log.emit(
                    f"Недопустимое значение B = {value_B}: число B должно быть от {self.value_A} до {self.value_C}")
        self.observers.emit()

    def get_value(self, value_type: Literal["A", "B", "C"]):
        return self.value_A if value_type == "A" else self.value_B if value_type == "B" else self.value_C

    def closeEvent(self, event: QCloseEvent):
        super().closeEvent(event)
        self.save_values()
