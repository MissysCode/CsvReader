import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
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

    def open_dialog(self):
        file_open = QFileDialog.getOpenFileName(self, "Open File", "", "Csv Files (*.csv)")
        if file_open[0]:
            csv_list, headers_row = self.csvreader.open_csv(file_open[0])

            self.model = DataModel(csv_list, headers_row)
            self.ui.tableView.setModel(self.model)
            self.ui.deleteButton.setEnabled(True)
        else:
            print("Cancel")
            return None

    def save_dialog(self):
        file_save = QFileDialog.getSaveFileName(self, "Save file", "", "Csv Files (*.csv)")
        if file_save[0]:
            self.csvreader.save_csv(file_save[0])

    def delete_row(self):
        reply = QMessageBox.question(self, "Delete", "Do you want to delete selected row?",
                                     QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            currentRow = self.ui.tableView.currentIndex().row()
            self.model.removeRow(currentRow)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
