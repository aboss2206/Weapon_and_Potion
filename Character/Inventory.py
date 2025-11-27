# Class for showing the player's inventory

class Inventory:
    def __init__(self):
        self.armor = {}
        self.weapons = {}
        self.potions = {}
        self.spells = {}

    def show_inventory(self, section="all"):
        if section == "all":
            print("Armor")
            print("-----")