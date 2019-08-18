import csv
import os


class Table:
    rulebook = ""
    name = ""
    rows = []

    def __init__(self, rulebook, file):
        self.rulebook = rulebook
        self.path = file
        self.rows = []
        self.name = self.fix_name(file)

        with open(file) as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                self.rows.append(row)
        csv_file.close()

    @staticmethod
    def fix_name(file):
        return os.path.splitext(os.path.basename(file))[0]

    def display_table(self):
        display = "--- " + self.name + " ---"
        print(display)
        self.rulebook.output.append(display)

    def get(self, item):
        for row in self.rows:
            if row['name'] == item:
                return row

    def get_list(self, command):
        result = []

        if len(command) == 1:
            for row in self.rows:
                result.append(row)
        elif len(command) == 2:
            for row in self.rows:
                if self.row_has_value(row, command[1]):
                    result.append(row)
        elif len(command) == 3:
            for row in self.rows:
                if self.row_has_key_and_value(row, command[1], command[2]):
                    result.append(row)
        return result

    @staticmethod
    def row_has_value(row, value):
        for k, v in row.items():
            if v == value:
                return True
        return False

    @staticmethod
    def row_has_key_and_value(row, key, value):
        for k, v in row.items():
            if k == key and v == value:
                return True
        return False
