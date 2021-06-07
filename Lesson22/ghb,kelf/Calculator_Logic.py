from Calculator_InterFace import *
from PyQt5.QtWidgets import QMessageBox


class Calculator(Ui_MainWindow):

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.add_func()
        self.is_equal = True

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
        self.button_delete.clicked.connect(lambda: self.write_number("-1"))
        self.button_open_brackets.clicked.connect(lambda: self.write_number(self.button_open_brackets.text()))
        self.button_close_brackets.clicked.connect(lambda: self.write_number(self.button_close_brackets.text()))
        self.button_dot.clicked.connect(lambda: self.write_number(self.button_dot.text()))
        self.del_button.clicked.connect(lambda: self.write_number("delete"))
        self.button_equal.clicked.connect(self.results)

    def write_number(self, number):

        if number == "delete":
            self.label.setText("0")
        elif number == "-1":
            self.label.setText(self.label.text()[0:-1])
        elif number == ".":
            self.label.setText(self.label.text() + number)
        elif self.is_equal is True and number.isdecimal():
            self.label.setText(number)
            self.is_equal = False
        elif self.label.text() == "-" and number.isdecimal():
            self.label.setText(self.label.text()+number)
            self.is_equal = False
        elif self.label.text() == "0" or self.label.text() == "+" or self.label.text() == "*" or self.label.text() == "/" or self.label.text() == "-":
            self.label.setText(number)
            self.is_equal = False
        else:
            self.label.setText(self.label.text() + number)
            self.is_equal = False

    def results(self):
        try:
            res = round(eval(self.label.text()),6)
            self.label.setText(str(res))
            self.is_equal = True
        except (SyntaxError, ZeroDivisionError, NameError):
            error = QMessageBox()
            error.setWindowTitle("Sho?")
            error.setText("Nel'tha")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Reset | QMessageBox.Ok | QMessageBox.Cancel)
            error.setDefaultButton(QMessageBox.Ok)
            error.setInformativeText("Tak delat' ne nado")
            error.setDetailedText("interesno?")
            error.buttonClicked.connect(self.popit_action)
            error.exec_()
            self.is_equal = True

    def popit_action(self, btn):
        if btn.text() == "Ok":
            print("Ok")
        elif btn.text() == "Reset":
            self.label.setText("0")
            self.is_equal = False


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Calculator()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
