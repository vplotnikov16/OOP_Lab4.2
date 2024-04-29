from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent, QCloseEvent
from PyQt5.QtWidgets import QMainWindow

from model import Model
from ..layouts.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.model = Model()
        self.model.observers.connect(self.update_from_model)
        self.model.log.connect(self.show_message)
        self.model.init_values()

        self.lineEdit_A.textEdited.connect(self.lineEdit_A_textEdited)
        self.lineEdit_B.textEdited.connect(self.lineEdit_B_textEdited)
        self.lineEdit_C.textEdited.connect(self.lineEdit_C_textEdited)

        self.spinBox_A.valueChanged.connect(self.spinBox_A_valueChanged)
        self.spinBox_B.valueChanged.connect(self.spinBox_B_valueChanged)
        self.spinBox_C.valueChanged.connect(self.spinBox_C_valueChanged)

        self.horizontalSlider_A.valueChanged.connect(self.horizontalSlider_A_valueChanged)
        self.horizontalSlider_B.valueChanged.connect(self.horizontalSlider_B_valueChanged)
        self.horizontalSlider_C.valueChanged.connect(self.horizontalSlider_C_valueChanged)

    def update_from_model(self):
        value_A = self.model.get_value("A")
        value_B = self.model.get_value("B")
        value_C = self.model.get_value("C")

        self.lineEdit_A.setText(str(value_A))
        self.lineEdit_B.setText(str(value_B))
        self.lineEdit_C.setText(str(value_C))

        self.spinBox_A.setValue(value_A)
        self.spinBox_B.setValue(value_B)
        self.spinBox_C.setValue(value_C)

        self.horizontalSlider_A.setValue(value_A)
        self.horizontalSlider_B.setValue(value_B)
        self.horizontalSlider_C.setValue(value_C)

    def show_message(self, text):
        self.statusbar.showMessage(text, 3000)

    def lineEdit_A_textEdited(self, text):
        if text.isnumeric():
            self.model.set_value(value_A=int(text))

    def lineEdit_B_textEdited(self, text):
        if text.isnumeric():
            self.model.set_value(value_B=int(text))

    def lineEdit_C_textEdited(self, text):
        if text.isnumeric():
            self.model.set_value(value_C=int(text))

    def spinBox_A_valueChanged(self, value):
        self.model.set_value(value_A=value)

    def spinBox_B_valueChanged(self, value):
        self.model.set_value(value_B=value)

    def spinBox_C_valueChanged(self, value):
        self.model.set_value(value_C=value)

    def horizontalSlider_A_valueChanged(self, value):
        self.model.set_value(value_A=value)

    def horizontalSlider_B_valueChanged(self, value):
        self.model.set_value(value_B=value)

    def horizontalSlider_C_valueChanged(self, value):
        self.model.set_value(value_C=value)

    def closeEvent(self, event: QCloseEvent):
        super().closeEvent(event)
        self.model.close()
