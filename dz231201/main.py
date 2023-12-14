import sys
# import os
# os.environ["QT_PLUGIN_PATH"] = "/usr/lib/qt/plugins"

from PyQt5 import QtWidgets, uic, QtCore
from module import App

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self.data = data

    def rowCount(self, parent):
        return len(self.data)

    def columnCount(self, parent):
        return len(self.data[0])

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            return str(self.data[index.row()][index.column()])


database_name = "my_database"
my_app = App(database_name)

app = QtWidgets.QApplication(sys.argv)

window = uic.loadUi("main.ui")

def save_purschase():

    is_done = window.is_done.isChecked()
    subject = window.subject.text()
    description_short = window.description_short.text()
    description = window.description.text()
    dt = window.dt.dateTime().toPyDateTime().isoformat()
    deadline = window.deadline.dateTime().toPyDateTime().isoformat()

    print(deadline, description, description_short, subject, is_done, dt)
    my_app.add_purchase(deadline, description, description_short, subject, is_done, dt)

    data = my_app.get_statistic()
    print(data)
    model = TableModel(data)
    window.table_view.setModel(model)

window.add_button.clicked.connect(save_purschase)

window.show()
app.exec()