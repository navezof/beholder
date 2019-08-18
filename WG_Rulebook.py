from rulebook import Rulebook


class WG_Rulebook(Rulebook):

    armor_table = "armor"
    weapon_table = "weapons"

    def __init__(self, root):
        self.root = root
        self.game = "wrathnglory"
        self.tables = []

        self.load_tables()

    def execute(self, command):
        self.output.clear()
        self.list(command)

        super().execute(command)

    def list(self, command):
        if command[0] == "list":
            self.display_rulebook()
            # self.list_armor()
            self.list_weapon(command)

    def list_armor(self):
        for table in self.tables:
            if table.name == self.armor_table:
                table.display_table()
                for row in table.rows:
                    self.display_armor(row)

    def list_weapon(self, command):
        for table in self.tables:
            if table.name == self.weapon_table:
                table.display_table()
                result = table.get_list(command)
                for row in result:
                    self.display_weapon(row)

    def display_armor(self, row):
        display = row['name'] + " - AR: " + row['armor rating']
        print(display)
        self.output.append(display)

    def display_weapon(self, row):
        display = row['name'] + " - dmg: " + row['damage']
        print(display)
        self.output.append(display)

    def display_item(self, table, row):
        if table.name == self.armor_table:
            self.display_armor(row)
        elif table.name == self.weapon_table:
            self.display_weapon(row)