import sys, csv, collections
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem, QFileDialog, QInputDialog, QMessageBox
from ui_csvreader import Ui_MainWindow
from csvmodel import MyModel

class MainWindow(QMainWindow, Ui_MainWindow):

	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.openButton.clicked.connect(self.open_dialog)
		self.saveButton.clicked.connect(self.save_dialog)

	def open_dialog(self):
		file_open = QFileDialog.getOpenFileName(self, 'Open File')
		if file_open[0]:
			self.open_csv(file_open[0])
		else:
			print ("Cancel")
			return None

	def save_dialog(self):
		file_save = QFileDialog.getSaveFileName(self, 'Save File', '/Documents/', '.csv')

	def open_csv(self, csvfile):
		csv_list = []
		headers_row = []
		first_row = True

		try:
			with open(csvfile, 'r') as csvfile:
				reader = csv.reader(csvfile)
				for row in reader:
					if (first_row):
						headers_row = row
						first_row = False
					else:
						csv_list.append(row)
				table = self.tableView
				model = MyModel(csv_list, headers_row)
				table.setModel(model)

		except Exception as e:
			QMessageBox.about(self, "Error", str(e))
			raise e

if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = MainWindow()
	w.show()
	sys.exit(app.exec_())
