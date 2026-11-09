# Class for showing the player's inventory
from Items.Item_types import Weapon, Armor, Potion, Spell

class Inventory:
    # Dictionaries to hold the different item categories {name: quantity}
    def __init__(self):
        self.armor = {}
        self.weapons = {}
        self.potions = {}
        self.spells = {}
        self.gold = 0
    
    # Functions for displaying each section
    def get_armor(self):
        return self.armor
            
    def get_weapons(self):
        return self.weapons

    def get_potions(self):
        return self.potions 

    def get_spells(self):
        return self.spells
    
    def get_gold(self):
        return self.gold

    def update_inventory(self, item_obj):
        if isinstance(item_obj, Weapon):
            if item_obj in self.weapons: # If item (key) is present, the item count (value) will be incremented
                self.weapons[item_obj] += 1
            else: # Otherwise, a new entry will be added with a count of 1
                self.weapons[item_obj] = 1
        elif isinstance(item_obj, Armor):
            if item_obj in self.weapons: 
                self.armor[item_obj] += 1
            else: 
                self.armor[item_obj] = 1

    def deposit_gold(self, amount):
        self.gold += amount

    def withdraw_gold(self, amount):
        self.gold -= amount