from rulebook import Rulebook


class DD_Rulebook(Rulebook):

    armor_table = "armor"
    spell_table = "spells"
    monster_table = "monster"

    def __init__(self, root):
        self.root = root
        self.game = "dnd"
        self.tables = []

        self.load_tables()

    def execute(self, command):
        self.output.clear()
        self.list(command)

        super().execute(command)

    def list(self, command):
        if command[0] == "list":
            self.display_rulebook()
            self.list_armor()
            self.list_spell()
            self.list_monster()

    def list_armor(self):
        for table in self.tables:
            if table.name == self.armor_table:
                table.display_table()
                for row in table.rows:
                    self.display_armor(row)

    def list_monster(self):
        for table in self.tables:
            if table.name == self.monster_table:
                table.display_table()
                for row in table.rows:
                    self.display_monster(row)

    def list_spell(self):
        for table in self.tables:
            if table.name == self.spell_table:
                table.display_table()
                for row in table.rows:
                    self.display_spell(row)

    def display_armor(self, row):
        display = row['name'] + " - AC: " + row['AC']
        print(display)
        self.output.append(display)

    def display_monster(self, row):
        display = row['name'] + " - CR: " + row['CR']
        print(display)
        self.output.append(display)

    def display_spell(self, row):
        display = row['name'] + " - " + row['description']
        print(display)
        self.output.append(display)

    def display_item(self, table, row):
        table.display_table()
        if table == self.armor_table:
            self.display_armor(row)
        elif table == self.spell_table:
            self.display_spell(row)
        elif table == self.monster_table:
            self.display_monster()
