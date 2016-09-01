from PyQt5.QtCore import *


class DataModel(QAbstractTableModel):
    def __init__(self, data=None, headerdata=None):
        super().__init__()
        if data:
            self.csv_data = data
            self.headers = headerdata

    def rowCount(self, parent=QModelIndex()):
        count = len(self.csv_data)
        return (count)

    def columnCount(self, parent=QModelIndex()):
        count = len(self.headers)
        return (count)

    def headerData(self, section, orientation, role):
        try:
            if role == Qt.DisplayRole and orientation == Qt.Horizontal:
                return QVariant(self.headers[section])
            if role == Qt.DisplayRole and orientation == Qt.Vertical:
                return QVariant(section + 1)
        except:
            pass

        return None

    def data(self, index, role):
        try:
            if role == Qt.DisplayRole:
                return self.csv_data[index.row()][index.column()]
        except:
            pass

        return None

    def removeRows(self, position, rows, index):
        self.beginRemoveRows(index, position, position + rows - 1)
        del self.csv_data[position:position + rows]
        self.endRemoveRows()

        return True
