# Class for showing the player's inventory

class Inventory:
    # Dictionaries to hold the different item categories
    def __init__(self):
        self.armor = {}
        self.weapons = {}
        self.potions = {}
        self.spells = {}
    
    # Functions for displaying each section
    def show_armor(self):
        print("- Armor -")
        for key, value in self.armor.items():
                print(f"{key} ({value})\n")
            
    def show_weapons(self):
        print("- Weapons -")
        for key, value in self.weapons.items():
                print(f"{key} ({value})\n")

    def show_potions(self):
        for key, value in self.potions.items():
                print(f"{key} ({value})\n")

    def show_spells(self):
        for key, value in self.potions.items():
                print(f"{key} ({value})\n")

    def update_inventory(self, item_name, section):
        if item_name in section: # If item (key) is present, the item count (value) will be incremented
            section[item_name] += 1
        else: # Otherwise, a new entry will be added with a count of 1
            section[item_name] = 1