# Item class
import random

# Item is a factory class which calls one of the derived item classes depending on the chosen item type
class Item:
    @classmethod
    def create(cls, player_level):
        types = ['Weapon', 'Armor', 'Potion', 'Spell']
        rand_type = random.choice(types)
        if rand_type == 'Weapon':
            return Weapon(player_level)
        
    # Static method for getting random key from a dictionary of items
    @staticmethod
    def random_item(dict):
        return random.choice(list(dict.items())) 

class Weapon(Item):
    def __init__(self, player_level):
        self.player_level = player_level
        name, (damage, damage_type) = self.generate_weapon()
        self.name = name
        self.damage = damage
        self.damage_type = damage_type

    def generate_weapon(self):
        low_level_weapons = {'Wood Sword': (2, 'P'), 'Wood Staff': (2, 'M')} # Dictionary which stores (weapon name: (damage, damage type)) where P = Physical, M = Magical
        med_level_weapons = low_level_weapons + {'Iron Sword': (4, 'P'), 'Iron Staff': (4, 'M')}
        high_level_weapons = med_level_weapons + {'Steel Sword': (6, 'P'), 'Steef Staff': (6, 'M')}
        rand_weapon = None
        if Item.player_level <= 5:
            rand_weapon = Item.random_item(low_level_weapons)
        elif Item.player_level > 5 and Item.player_level < 10:
            rand_weapon = Item.random_item(med_level_weapons)
        else:
            rand_weapon = Item.random_item(high_level_weapons)
        return rand_weapon
        
class Armor(Item):
    def __init__(self, player_level):
        self.player_level = player_level
        weapon_name, weapon_damage = self.generate_weapon()
        self.name = weapon_name
        self.damage = weapon_damage

    def generate_armor(self):
        low_level_weapons = {'Wood Sword': 2, 'Wood Staff': 2} # Dictionary which stores: [armor name: (physical defence, magical defence)]
        med_level_weapons = low_level_weapons + {'Iron Sword': 4, 'Iron Staff': 4}
        high_level_weapons = med_level_weapons + {'Steel Sword': 6, 'Steef Staff': 6}
        rand_weapon = None
        if Item.player_level <= 5:
            rand_weapon = Item.random_item(low_level_weapons)
        elif Item.player_level > 5 and Item.player_level < 10:
            rand_weapon = Item.random_item(med_level_weapons)
        else:
            rand_weapon = Item.random_item(high_level_weapons)
        return rand_weapon