import os
import csv

rulebook = []
result = []

display_result = True
rule_folder = "./"


class Settings:
    display_result = True
    rule_folder = "./"

class RuleSet:
    def __init__(self, name, csvfile):
        self.name = name
        self.rule = []

        with open(csvfile) as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                self.rule.append(row)
            csv_file.close()

    def execute(self, command):
        if command[0] == "list" or command[0] == self.name:
            self.list(command)
        elif command[0] == "tables":
            self.display_text(self.name)
        else:
            self.fetch(command)

    def fetch(self, command):
        for row in self.rule:
            if row['item'] == command[0]:
                self.display(row)

    def list(self, command):
        if len(command) == 4 and command[1] == self.name:
            self.display_text(self.name + " (" + command[2] + ": " + command[3] + ")")
            for row in self.rule:
                for key, value in row.items():
                    if key == command[2] and value == command[3]:
                        self.display(row)

        elif len(command) == 3 and command[1] == self.name:
            self.display_text(self.name + " (" + command[2] + ")")
            for row in self.rule:
                for key, value in row.items():
                    if value == command[2]:
                        self.display(row)

        elif len(command) == 3:
            for rule in rulebook:
                if command[1] == rule.name and rule.name != self.name:
                    return

            self.display_text(self.name + " (" + command[1] + ": " + command[2] + ")")
            for row in self.rule:
                for key, value in row.items():
                    if key == command[1] and value == command[2]:
                        self.display(row)

        elif len(command) == 1 or (len(command) == 2 and command[1] == self.name):
            self.display_text(self.name)
            for row in self.rule:
                self.display(row)

        elif len(command) == 2:
            for rule in rulebook:
                if command[1] == rule.name and rule.name != self.name:
                    return

            self.display_text(self.name + " (" + command[1] + ")")
            for row in self.rule:
                for key, value in row.items():
                    if value == command[1]:
                        self.display(row)

    @staticmethod
    def display_text(text):
        result.append("--- " + text + " ---")

        if display_result:
            print("--- " + text + " ---")
        else:
            return


class WeaponRule(RuleSet):

    @staticmethod
    def display(row):
        result.append(row['item'] + ' - damage:' + row['damage'] + ' (' + row['traits'] + ')')

        if display_result:
            print(row['item'] + ' - damage:' + row['damage'] + ' (' + row['traits'] + ')')
        else:
            return


class ArmorRule(RuleSet):

    @staticmethod
    def display(row):
        result.append(row['item'] + ' - AR:' + row['armor rating'])

        if display_result:
            print(row['item'] + ' - AR:' + row['armor rating'])
        else:
            return


####

def fix_quotes(input):
    fixed_command = []
    wait_for_end_of_quote = False
    for s in input:
        if wait_for_end_of_quote:
            fixed_command[-1] = fixed_command[-1] + " " + s.replace('\"', '')
            if "\"" in s:
                wait_for_end_of_quote = False
        elif s[0] == "\"":
            fixed_command.append(s.replace("\"", ""))
            wait_for_end_of_quote = True
        else:
            fixed_command.append(s)
    return fixed_command


def setup(folder):

    armor = ArmorRule("armors", folder + "armor.csv")
    rulebook.append(armor)

    weapons = WeaponRule("weapons", folder + "weapons.csv")
    rulebook.append(weapons)

def execute(command):
    if command[0] == "help":
        help()
    for rule in rulebook:
        rule.execute(command)


def update():
    command = ""
    while command != "exit":
        command = input("\n>")
        parsed_string = fix_quotes(command.split())
        execute(parsed_string)


def help():
    print("Available command:\n")
    print("\ttables\t\t\t\tDisplay all currently loaded table")
    print("\tlist\t\t\t\tDisplay all item currently loaded")
    print("\t<table name>\t\t\tDisplay content of a table")
    print("\tlist <table>\t\t\tDisplay content of a table")
    print("\t<item>\t\t\t\tDisplay stat of an item within all tables")
    print("\tlist <value>\t\t\tDisplay all item having this value")
    print("\tlist <attribute> <value>\tDisplay all item having this value for this specific attribute")
    print("\thelp\t\t\t\tBring the list of available command")
    print("\texit\t\t\t\tExit the application")


if __name__ == "__main__":
    print("--- BEHOLDER ---")

    setup(rule_folder)
    help()
    update()
