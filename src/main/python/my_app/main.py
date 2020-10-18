import sys
import json
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt


qt_creator_file = "src\\tutorials\\mainwindowTable.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_creator_file)


class TodoModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TodoModel, self).__init__()
        self._data = data
        self.header_labels = ['Name', 'Initiative', 'AC', 'HP']

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.header_labels[section]
        return QtCore.QAbstractTableModel.headerData(self, section, orientation, role)
        
    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)


    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        #QtWidgets.QMainWindow.__init__(self)
        #Ui_MainWindow.__init__(self)
        data = [
          ["Ghurrix", 9, 1, 6],
          ["Valmet", 20,19,143],
        ]
        self.model = TodoModel(data)
        #self.load()
        self.setupUi(self)
        self.tableView.setModel(self.model)
        self.addButton.pressed.connect(self.add)
        #self.deleteButton.pressed.connect(self.delete)
        #self.completeButton.pressed.connect(self.complete)
        

    def add(self):
        """
        Add an item to our todo list, getting the text from the QLineEdit .todoEdit
        and then clearing it.
        """
        text = self.todoEdit.text()
        if text: # Don't add empty strings.
            # Access the list via the model.
            self.model._data.append((False, text))
            # Trigger refresh.        
            self.model.layoutChanged.emit()
            # Empty the input
            self.todoEdit.setText("")
            self.save()          
    
    def load(self):
        try:
            with open('src\\tutorials\\data.db', 'r') as f:
                self.model._data = json.load(f)
        except Exception:
            pass

    def save(self):
        with open('src\\tutorials\\data.db', 'w') as f:
            data = json.dump(self.model._data, f)

    
    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()


