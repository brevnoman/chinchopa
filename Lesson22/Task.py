import PyQt5
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 400)
        self.centralwidget = PyQt5.QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = PyQt5.QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(PyQt5.QtCore.QRect(0, 0, 300, 50))
        font = PyQt5.QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.button0 = PyQt5.QtWidgets.QPushButton(self.centralwidget)
        self.button0.setGeometry(PyQt5.QtCore.QRect(0, 260, 150, 90))
        self.button0.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.button0.setObjectName("button0")
        self.button_equal = PyQt5.QtWidgets.QPushButton(self.centralwidget)
        self.button_equal.setGeometry(PyQt5.QtCore.QRect(150, 320, 150, 90))
        self.button_equal.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(255, 255, 255);")
        self.button_equal.setObjectName("button_equal")
        self.button7 = PyQt5.QtWidgets.QPushButton(self.centralwidget)
        self.button7.setGeometry(PyQt5.QtCore.QRect(0, 50, 100, 70))
        self.button7.setObjectName("button7")
        self.button8 = PyQt5.QtWidgets.QPushButton(self.centralwidget)
        self.button8.setGeometry(PyQt5.QtCore.QRect(100, 50, 100, 70))
        self.button8.setObjectName("button8")
        self.button9 = PyQt5.QtWidgets.QPushButton(self.centralwidget)
        self.button9.setGeometry(PyQt5.QtCore.QRect(200, 50, 100, 70))
        self.button9.setObjectName("button9")
        self.button4 = PyQt5.QtWidgets.QPushButton(self.centralwidget)
        self.button4.setGeometry(PyQt5.QtCore.QRect(0, 120, 100, 70))
        self.button4.setObjectName("button4")
        self.button5 = PyQt5.QtWidgets.QPushButton(self.centralwidget)
        self.button5.setGeometry(PyQt5.QtCore.QRect(100, 120, 100, 70))
        self.button5.setObjectName("button5")
        self.button6 = PyQt5.QtWidgets.QPushButton(self.centralwidget)
        self.button6.setGeometry(PyQt5.QtCore.QRect(200, 120, 100, 70))
        self.button6.setObjectName("button6")
        self.button1 = PyQt5.QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(PyQt5.QtCore.QRect(0, 190, 100, 70))
        self.button1.setObjectName("button1")
        self.button2 = PyQt5.QtWidgets.QPushButton(self.centralwidget)
        self.button2.setGeometry(PyQt5.QtCore.QRect(100, 190, 100, 70))
        self.button2.setObjectName("button2")
        self.button3 = PyQt5.QtWidgets.QPushButton(self.centralwidget)
        self.button3.setGeometry(PyQt5.QtCore.QRect(200, 190, 100, 70))
        self.button3.setObjectName("button3")
        self.plus_button = PyQt5.QtWidgets.QPushButton(self.centralwidget)
        self.plus_button.setGeometry(PyQt5.QtCore.QRect(150, 259, 75, 60))
        self.plus_button.setObjectName("plus_button")
        self.minus_button = PyQt5.QtWidgets.QPushButton(self.centralwidget)
        self.minus_button.setGeometry(PyQt5.QtCore.QRect(225, 259, 75, 60))
        self.minus_button.setObjectName("minus_button")
        self.mult_button = PyQt5.QtWidgets.QPushButton(self.centralwidget)
        self.mult_button.setGeometry(PyQt5.QtCore.QRect(0, 348, 75, 60))
        self.mult_button.setObjectName("mult_button")
        self.division_button = PyQt5.QtWidgets.QPushButton(self.centralwidget)
        self.division_button.setGeometry(PyQt5.QtCore.QRect(73, 349, 75, 60))
        self.division_button.setObjectName("division_button")
        self.button_delete = PyQt5.QtWidgets.QPushButton(self.centralwidget)
        self.button_delete.setGeometry(PyQt5.QtCore.QRect(250, 0, 50, 50))
        self.button_delete.setObjectName("button_delete")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        PyQt5.QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_func()
        self.is_equal = False

    def retranslateUi(self, MainWindow):
        _translate = PyQt5.QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.label.setText(_translate("MainWindow", "0"))
        self.button0.setText(_translate("MainWindow", "0"))
        self.button_equal.setText(_translate("MainWindow", "="))
        self.button7.setText(_translate("MainWindow", "7"))
        self.button8.setText(_translate("MainWindow", "8"))
        self.button9.setText(_translate("MainWindow", "9"))
        self.button4.setText(_translate("MainWindow", "4"))
        self.button5.setText(_translate("MainWindow", "5"))
        self.button6.setText(_translate("MainWindow", "6"))
        self.button1.setText(_translate("MainWindow", "1"))
        self.button2.setText(_translate("MainWindow", "2"))
        self.button3.setText(_translate("MainWindow", "3"))
        self.plus_button.setText(_translate("MainWindow", "+"))
        self.minus_button.setText(_translate("MainWindow", "-"))
        self.mult_button.setText(_translate("MainWindow", "*"))
        self.division_button.setText(_translate("MainWindow", "/"))
        self.button_delete.setText(_translate("MainWindow", "<"))


    def add_func(self):
        self.button0.clicked.connect(lambda: self.write_number(self.button0.text()))
        self.button1.clicked.connect(lambda: self.write_number(self.button1.text()))
        self.button2.clicked.connect(lambda: self.write_number(self.button2.text()))
        self.button3.clicked.connect(lambda: self.write_number(self.button3.text()))
        self.button4.clicked.connect(lambda: self.write_number(self.button4.text()))
        self.button5.clicked.connect(lambda: self.write_number(self.button5.text()))
        self.button6.clicked.connect(lambda: self.write_number(self.button6.text()))
        self.button7.clicked.connect(lambda: self.write_number(self.button7.text()))
        self.button8.clicked.connect(lambda: self.write_number(self.button8.text()))
        self.button9.clicked.connect(lambda: self.write_number(self.button9.text()))
        self.division_button.clicked.connect(lambda: self.write_number(self.division_button.text()))
        self.mult_button.clicked.connect(lambda: self.write_number(self.mult_button.text()))
        self.plus_button.clicked.connect(lambda: self.write_number(self.plus_button.text()))
        self.minus_button.clicked.connect(lambda: self.write_number(self.minus_button.text()))
        self.button_delete.clicked.connect(lambda: self.write_number(" "))

        self.button_equal.clicked.connect(self.results)

    def write_number(self, number):
        if self.label.text() == "0" or self.is_equal or self.label.text() == "+" or self.label.text() == "*" or self.label.text() == "/" or number == " ":
            self.label.setText(number)
            self.is_equal = False
        else:
            self.label.setText(self.label.text() + number)

    def results(self):
        if self.is_equal or self.label.text()[0] == "+" or self.label.text()[0] == "*" or self.label.text()[
            0] == "/" or self.label.text() == "-" or self.label.text() == " ":
            error = QMessageBox()
            error.setWindowTitle("Ohuel?")
            error.setText("Nel'tha")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Reset | QMessageBox.Ok | QMessageBox.Cancel)
            error.setDefaultButton(QMessageBox.Ok)
            error.setInformativeText("Tak delat' ne nado")
            error.setDetailedText("interesno?")
            error.buttonClicked.connect(self.popit_action)
            error.exec_()
            self.is_equal = True
        else:
            res = eval(self.label.text())
            self.label.setText(str(res))
            self.is_equal = True

    def popit_action(self, btn):
        if btn.text() == "Ok":
            print("Ok")
        elif btn.text() == "Reset":
            self.label.setText("")
            self.is_equal = False


if __name__ == "__main__":
    import sys

    app = PyQt5.QtWidgets.QApplication(sys.argv)
    MainWindow = PyQt5.QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
