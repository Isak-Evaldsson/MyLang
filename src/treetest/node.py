class nodeTree:
    def __init__(self, name, *children):
        self.name, self.children = name, children

    def __str__(self, level=0):
        ret = "\t" * level + self.name + "\n"

        for child in self.children:
            ret += child.__str__(level + 1)

        return ret

    def print(self):
        print(self.__str__())
