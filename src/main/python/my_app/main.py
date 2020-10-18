from PyQt5 import QtWidgets, uic
import sys

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("ui\\test3.ui", self)

        #self.button = self.findChild(QtWidgets.QPushButton, 'pushButton') # Find the button
        #self.button.clicked.connect(self.printButtonPressed) # Remember to pass the definition/method, not the return value!

        self.pushButton.clicked.connect(self.printButtonPressed) # Remember to pass the definition/method, not the return value!

        self.show()

    def printButtonPressed(self):
        # This is executed when the button is pressed
        print('printButtonPressed')



app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
