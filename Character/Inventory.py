# Class for showing the player's inventory
from Items.Item_types import Weapon, Armor, Potion, Spell

class Inventory:
    # Dictionaries to hold the different item categories (Item name: Quantity)
    def __init__(self):
        self.armor = {}
        self.weapons = {}
        self.potions = {}
        self.spells = {}
        self.gold = 0
    
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

    def update_inventory(self, item_obj):
        if isinstance(item_obj, Weapon):
            if item_obj.name in self.weapons: # If item (key) is present, the item count (value) will be incremented
                self.weapons[item_obj] += 1
            else: # Otherwise, a new entry will be added with a count of 1
                self.weapons[item_obj] = 1

    def get_gold(self):
        return self.gold

    def deposit_gold(self, amount):
        self.gold += amount

    def withdraw_gold(self, amount):
        self.gold -= amount