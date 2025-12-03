# Item class
import random

class Item:
    def __init__(self, player_level):
        self.player_level = player_level
        self.type = self.generate_type()

    def generate_type(self):
        types = ['Weapon', 'Armor', 'Potion', 'Spell']
        rand_index = types[random.randint(0, len(types))]
        return types[rand_index]

class Weapon(Item):
    def __init__(self, name, damage):
        weapon_name, weapon_damage = self.generate_weapon()
        self.name = weapon_name
        self.damage = weapon_damage

    def generate_weapon(self):
        low_level_weapons = {'Wood Sword': 2, 'Wood Staff': 2} # Dictionary which stores weapon name (key) and damage (value)
        med_level_weapons = low_level_weapons + {{'Iron Sword': 4}, {'Iron Staff': 4}}
        high_level_weapons = med_level_weapons + {'Steel Sword', 'Steef Staff'}
        random_index = None
        if Item.player_level <= 5:
            random_index = random.randint(0, len(low_level_weapons)) # Generate random index
            return low_level_weapons[random_index]
        elif Item.player_level > 5 and Item.player_level < 10:
            random_index = random.randint(0, len(med_level_weapons))
            return med_level_weapons[random_index]
        else:
            random_index = random.randint(0, len(high_level_weapons)) 
            return high_level_weapons[random_index]