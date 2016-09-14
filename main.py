import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QInputDialog
from ui_csvreader import Ui_MainWindow
from csvmodel import DataModel
from csvreader import Csvreader

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.model = DataModel(self)
        self.csvreader = Csvreader()

        self.ui.openButton.clicked.connect(self.open_dialog)
        self.ui.saveButton.clicked.connect(self.save_dialog)
        self.ui.deleteButton.clicked.connect(self.delete_row)
        self.ui.mergeButton.clicked.connect(self.merge_files)

    def open_dialog(self):
        file_open = QFileDialog.getOpenFileName(self, "Open File", "", "Csv Files (*.csv)")
        if file_open[0]:
            #clear tableview first and then set new data to model and model to tableview
            self.model = DataModel()
            self.ui.tableView.setModel(self.model)
            csv_list, headers_row = self.csvreader.open_csv(file_open[0])   
            self.model = DataModel(csv_list, headers_row)
            self.ui.tableView.setModel(self.model)
            self.ui.deleteButton.setEnabled(True)
        else:
            print("Cancel")
            return None

    def save_dialog(self):
        #save current datamodel to file
        file_save = QFileDialog.getSaveFileName(self, "Save file", "", "Csv Files (*.csv)")
        if file_save[0]:
            data_save = self.model.csv_data
            headers_save = self.model.headers
            self.csvreader.save_csv(file_save[0], data_save, headers_save)

    def delete_row(self):
        reply = QMessageBox.question(self, "Delete", "Delete selected row?",
                                     QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            currentRow = self.ui.tableView.currentIndex().row()
            self.model.removeRow(currentRow)

    def merge_files(self):
        #get current data from tableview and combine it with data from the new file
        data1 = self.model.csv_data
        headers1 = self.model.headers
        if headers1:
            file_merge = QFileDialog.getOpenFileName(self, "Merge File", "", "Csv Files (*.csv)")
            if file_merge[0]:
                data2, headers2 = self.csvreader.open_csv(file_merge[0])
                data = self.csvreader.merge(data1, data2)
                self.model = DataModel(data, headers1)
                self.ui.tableView.setModel(self.model)

        else:
            QMessageBox.about(self, "Error", "No file open")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
