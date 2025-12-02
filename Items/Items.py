# Item class
import random

class Item:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def generate_type(self):
        types = ['Weapon', 'Armor', 'Potion', 'Spell']


class Weapon(Item):
    def generate_weapon(self, player_level):
        low_level_weapons = {'Wood Sword', 'Wood Staff'}
        med_level_weapons = low_level_weapons + {'Iron Sword', 'Iron Staff'}
        high_level_weapons = med_level_weapons + {'Steel Sword', 'Steef Staff'}
        
