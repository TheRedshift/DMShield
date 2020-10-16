from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("ui\\test3.ui", self)

        self.button = self.findChild(QtWidgets.QPushButton, 'pushButton') # Find the button
        self.button.clicked.connect(self.printButtonPressed) # Remember to pass the definition/method, not the return value!

        self.button = self.findChild(QtWidgets.QPushButton, 'sortButton') # Find the button
        self.button.clicked.connect(self.sortButtonPressed) # Remember to pass the definition/method, not the return value!

        self.show()

    def printButtonPressed(self):
        # This is executed when the button is pressed
        print('printButtonPressed')

    def sortButtonPressed(self):
        # This is executed when the button is pressed
        print('sortButtonPressed')

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
