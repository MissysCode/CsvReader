import sys, csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem, QFileDialog, QInputDialog, QMessageBox
from ui_csvreader import Ui_MainWindow
from csvmodel import MyModel

class MainWindow(QMainWindow, Ui_MainWindow):

	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.actionOpen_csv_file.triggered.connect(self.open_dialog)

	def open_dialog(self):
		key_input = QInputDialog.getText(self, 'Input Dialog', 'Input key?')
		self.headerkey = key_input[0]
		file_open = QFileDialog.getOpenFileName(self, 'Open File')
		if file_open[0]:
			self.open_csv(file_open[0])
		else:
			print ("Cancel")
			return None

	def open_csv(self, csvfile):
		csv_dict = {}
		headers_row = []
		first_row = True

		try:
			with open(csvfile, 'r') as csvfile:
				reader = csv.reader(csvfile)
				for row in reader:
					if (first_row):
						headers_row = row
						if self.headerkey not in row:
							QMessageBox.about(self, "Error", "No \"" + self.headerkey + "\" in headers, can't process.")
							return None
						else:
							print (self.headerkey)
							key_index = row.index(self.headerkey)
							first_row = False
					else:
						csv_dict[(row[key_index])] = row
				table = self.tableView
				model = MyModel(csv_dict, headers_row)
				table.setModel(model)

		except Exception as e:
			raise e

if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = MainWindow()
	w.show()
	sys.exit(app.exec_())
