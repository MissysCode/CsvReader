import csv

class Csvreader():
    def open_csv(self, openfile):
        #get and return data and headers from .csv-file
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
            raise e

    def save_csv(self, savefile, data, headers):
        #save current data from model as a .csv-file
        try:
            with open(savefile, 'w') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(headers)
                writer.writerows(data)

        except Exception as e:
            raise e

    def merge(self, a_data, b_data):
        #merge datasets, using headers from first
        keys = []
        key_index = 3

        for a in a_data:
            keys.append(a[key_index])

        data = a_data

        for b in b_data:
            if b[key_index] not in keys:
                data.append(b)

        return data







