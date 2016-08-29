from PyQt5.QtCore import *

class MyModel(QAbstractTableModel):

	def __init__(self, data = None, headerdata = None):
		super().__init__()
		if data:
			self.csv_data = data
			self.headers = headerdata

	def rowCount(self, parent):
		count = len(self.csv_data)
		return (count)

	def columnCount(self, parent):
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

	def removeRow(self, position, rows=1, index=QModelIndex()):
		self.beginRemoveRows(QModelIndex(), position, position)
		self.endRemoveRows()

