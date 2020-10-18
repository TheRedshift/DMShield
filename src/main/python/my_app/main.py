import sys
import json
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from fbs_runtime.application_context.PyQt5 import ApplicationContext


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
            if index.column() != 0:
                return int(self._data[index.row()][index.column()])
            else:   
                return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)


    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        if len(self._data) > 0:
            return len(self._data[0])
        else:
            return 0

    def setData(self, index, value, role):
        if value != "":
            self._data[index.row()][index.column()] = value
        return True

    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

class MyDelegate(QtWidgets.QItemDelegate):

    def createEditor(self, parent, option, index):
        return super(MyDelegate, self).createEditor(parent, option, index)

    def setEditorData(self, editor, index):
        # Gets display text if edit data hasn't been set.
        text = index.data(Qt.EditRole) or index.data(Qt.DisplayRole)
        editor.setText(str(text))    

    def setModelData(self, editor, model, index):
        model.setData(index, editor.text())


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        #QtWidgets.QMainWindow.__init__(self)
        #Ui_MainWindow.__init__(self)
        data = [
          ["Name here", 1, 2, 3],
        ]
        self.model = TodoModel(data)
        self.proxyModel = QtCore.QSortFilterProxyModel()
        self.proxyModel.setSourceModel(self.model)
        #tableView.setModel(proxyModel)
        #tableView.setSortingEnabled(True)
        self.load()
        self.setupUi(self)
        self.tableView.setModel(self.proxyModel)
        self.delegate = MyDelegate()
        self.tableView.setItemDelegate(self.delegate)
        self.addButton.pressed.connect(self.add)
        self.deleteSelected.pressed.connect(self.delete)
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
            self.model._data.append(text.split(","))
            # Trigger refresh.        
            self.model.layoutChanged.emit()
            # Empty the input
            self.todoEdit.setText("")
            self.save()          
    
    def delete(self):
        indexes = self.tableView.selectedIndexes()
        if indexes:
            # Indexes is a list of a single item in single-select mode.
            index = indexes[0]
            # Remove the item and refresh.
            del self.model._data[index.row()]
            self.model.layoutChanged.emit()
            # Clear the selection (as it is no longer valid).
            self.tableView.clearSelection()
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


appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
sys.exit(exit_code)
app.exec_()


