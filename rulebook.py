import csv
import os

from Table import Table


class Rulebook:
    root = ""
    game = ""
    tables = []
    output = []

    def load_tables(self):
        self.tables.clear()
        for r, dirs, files in os.walk(self.root + "/" + self.game):
            for file in files:
                new_table = Table(self, self.root + "/" + self.game + "/" + file)
                self.tables.append(new_table)

    def execute(self, command):
        self.cmd_rulebook(command)
        self.cmd_tables(command)
        self.cmd_fetch(command)
        return self.output

    def cmd_fetch(self, command):
        for table in self.tables:
            result = table.get(command[0])
            if result:
                self.display_rulebook()
                table.display_table()
                self.display_item(table, result)

    def cmd_rulebook(self, command):
        if command[0] == "rulebooks":
            self.display_rulebook()

    def cmd_tables(self, command):
        if command[0] == "tables":
            self.display_tables()

    def display_rulebook(self):
        display = "=== " + self.game + " ==="
        print(display)
        self.output.append(display)

    def display_tables(self):
        self.display_rulebook()
        for table in self.tables:
            table.display_table()
