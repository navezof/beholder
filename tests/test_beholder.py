import unittest

from beholder import Beholder


class MyTestCase(unittest.TestCase):
    test_rule_folder = "../rulebooks"

    def test_rulebooks(self):
        command = ["rulebooks"]
        obtained = []
        expected = ['=== wrathnglory ===', '=== dnd ===']

        beholder = Beholder()
        beholder.load_rulebooks(self.test_rule_folder)
        obtained = beholder.run(command)

        self.assertEqual(expected, obtained)

    def test_tables(self):
        command = ["tables"]
        obtained = []
        expected = ['=== wrathnglory ===',
                    '--- armor ---',
                    '--- weapons ---',
                    '=== dnd ===',
                    '--- armor ---',
                    '--- monster ---',
                    '--- spells ---']

        print("\n>" + "".join(command))
        beholder = Beholder()
        beholder.load_rulebooks(self.test_rule_folder)
        obtained = beholder.run(command)

        self.assertEqual(expected, obtained)

    def test_list(self):
        command = ["list"]
        obtained = []
        expected = ['=== wrathnglory ===',
                    '--- armor ---',
                    'flak coat - AR: 3',
                    'flak vest - AR: 3',
                    'plate armor - AR: 4',
                    '--- weapons ---',
                    'shotgun - dmg: 10+1ED',
                    'lasgun - dmg: 7+1ED',
                    'bolt pistol - dmg: 7+1ED',
                    'power sword - dmg: 10+1ED',
                    'power axe - dmg: 12+2ED',
                    '=== dnd ===',
                    '--- armor ---',
                    'plate - AC: 16',
                    'leather armor - AC: 13',
                    '--- spells ---',
                    'fireball - fireball_description',
                    'magic missile - magic_description',
                    '--- monster ---',
                    'goblin - CR: 1',
                    'bandit - CR: 2']

        print("\n>" + "".join(command))
        beholder = Beholder()
        beholder.load_rulebooks(self.test_rule_folder)
        obtained = beholder.run(command)

        self.assertEqual(expected, obtained)

    def test_fetch_item(self):
        command = ["shotgun"]
        obtained = []
        expected = ['=== wrathnglory ===', '--- weapons ---', 'shotgun - dmg: 10+1ED']

        print("\n>" + "".join(command))
        beholder = Beholder()
        beholder.load_rulebooks(self.test_rule_folder)
        obtained = beholder.run(command)

        self.assertEqual(expected, obtained)

    def test_fetch_all_item_with_attribute(self):
        command = ["list", "ranged"]
        obtained = []
        expected = ['=== wrathnglory ===',
                    '--- weapons ---',
                    'shotgun - dmg: 10+1ED',
                    'lasgun - dmg: 7+1ED',
                    'bolt pistol - dmg: 7+1ED']

        print("\n>" + "".join(command))
        beholder = Beholder()
        beholder.load_rulebooks(self.test_rule_folder)
        obtained = beholder.run(command)

        self.assertEqual(expected, obtained)


if __name__ == '__main__':
    unittest.main()
