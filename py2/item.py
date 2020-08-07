class Item:
    def __init__(self, id, name, description):
        self.name = name
        self.id = id
        self.description = description

    def __str__(self):
        return f"{self.name}"