class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []

    def __str__(self):
        return(f"{self.name}, {self.description}")

    def room_description(self):
        return(f"{self.description}")

    def displayItems(self):
        items = []
        for item in self.items:
            items.append(item.name)
        return items

    # def print_items(self):
    #     for name in enumerate(self.items):
    #         print(f"{name}")

# class Room:
#     def __init__(self, name, desc):
#         self.name = name
#         self.desc = desc