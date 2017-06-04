class Player:

    def __init__(self, ID, name, health, items):
        self.ID = ID
        self.name = name
        self.health = health
        self.items = items


    def __str__(self):
        return "My ID: " + str(self.ID) + \
            " \nMy Name: " + str(self.name) +\
            " \nMy Health: " + str(self.health) +\
            " \nMy Items: " + str(self.items)+ "."
