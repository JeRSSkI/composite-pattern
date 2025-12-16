from component import Component

class File(Component):
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"File: {self.name}")
