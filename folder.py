from component import Component

class Folder(Component):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def show(self):
        print(f"Folder: {self.name}")
        for child in self.children:
            child.show()
