import os

from DD_Rulebook import DD_Rulebook
from WG_Rulebook import WG_Rulebook
from rulebook import Rulebook


class Beholder:
    debug = True
    rule_folder = "./rulebooks"

    rulebooks = []


    def run(self, command):
        output = []

        for rulebook in self.rulebooks:
            rulebook.execute(command)
            output.extend(rulebook.output)
        return output

    def update(self):
        command = ["list"]

        for rulebook in self.rulebooks:
            rulebook.execute(command)

    def load_rulebooks(self):
        self.rulebooks.clear()
        self.rulebooks.append(WG_Rulebook(self.rule_folder))
        self.rulebooks.append(DD_Rulebook(self.rule_folder))

    def load_rulebooks(self, path):
        self.rulebooks.clear()
        self.rulebooks.append(WG_Rulebook(path))
        self.rulebooks.append(DD_Rulebook(path))

    def start(self):
        print("start")
        self.load_rulebooks()
        self.update()


if __name__ == "__main__":
    beholder = Beholder()
    beholder.start()
