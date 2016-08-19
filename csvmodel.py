from PyQt5.QtCore import *

class MyModel(QAbstractTableModel):

	def __init__(self, data, headerdata):
		super().__init__()
		if data:
			self.csvdict = data
			self.headers = headerdata
			self.ldata = list(self.csvdict.values())

	def rowCount(self, parent):
		count = len(self.csvdict)
		return (count)

	def columnCount(self, parent):
		count = len(self.csvdict.values())
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
				return self.ldata[index.row()][index.column()]
		except:
			pass

		return None


