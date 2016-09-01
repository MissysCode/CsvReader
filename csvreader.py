import csv
from PyQt5.QtWidgets import QMessageBox

class Csvreader():
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

            return csv_list, headers_row

        except Exception as e:
            QMessageBox.about(self, "Error", str(e))
            raise e

    def save_csv(self, savefile, data, headers):
        try:
            with open(savefile, 'w') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(headers)
                writer.writerows(data)

        except Exception as e:
            QMessageBox.about(self, "Error", str(e))
            raise e