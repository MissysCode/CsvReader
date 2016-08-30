import sys, csv
from collections import namedtuple
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem, QFileDialog, QInputDialog, QMessageBox
from ui_csvreader import Ui_MainWindow
from csvmodel import MyModel


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.model = MyModel(self)

        self.ui.openButton.clicked.connect(self.open_dialog)
        self.ui.saveButton.clicked.connect(self.save_dialog)
        self.ui.deleteButton.clicked.connect(self.delete_row)

    def open_dialog(self):
        file_open = QFileDialog.getOpenFileName(self, "Open File", "", "Csv Files (*.csv)")
        if file_open[0]:
            self.open_csv(file_open[0])
        else:
            print("Cancel")
            return None

    def save_dialog(self):
        file_save = QFileDialog.getSaveFileName(self, "Save file", "", "Csv Files (*.csv)")
        if file_save[0]:
            self.save_csv(file_save[0])

    def delete_row(self):
        reply = QMessageBox.question(self, "Delete", "Do you want to delete selected row?",
                                     QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            currentRow = self.ui.tableView.currentIndex().row()
            self.model.removeRow(currentRow)

    def open_csv(self, openfile):
        csv_list = []
        headers_row = []
        first_row = True

        try:
            with open(openfile, 'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if (first_row):
                        headers_row = row
                        first_row = False
                    else:
                        csv_list.append(row)
                self.model = MyModel(csv_list, headers_row)
                self.ui.tableView.setModel(self.model)
                self.ui.deleteButton.setEnabled(True)

        except Exception as e:
            QMessageBox.about(self, "Error", str(e))
            raise e

    def save_csv(self, savefile):
        try:
            with open(savefile, 'w') as csvfile:
                writer = csv.writer(csvfile)

        except Exception as e:
            QMessageBox.about(self, "Error", str(e))
            raise e


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
