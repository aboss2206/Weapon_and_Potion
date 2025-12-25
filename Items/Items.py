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
        self.name, self.damage, self.damage_type = name, damage, damage_type

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
        self.name, self.damage = weapon_name, weapon_damage

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
    
class Potion(Item):
    def __init__(self, player_level):
        self.player_level = player_level
        name, restoration = self.generate_potion()
        self.potion_name, self.potion_restoration = name, restoration

    def generate_potion(self):
        # Dictionary which stores: [potion name: restoration amount]
        small_potions = {'Small Health Potion': 2, 'Small Energy Potion': 2, 'Small Magic Potion': 2} 
        medium_potions = small_potions + {'Medium Health Potion': 4, 'Medium Energy Potion': 4, 'Medium Magic Potion': 4} 
        large_potions = medium_potions + {'Large Health Potion': 6, 'Large Energy Potion': 6, 'Large Magic Potion': 6} 
        rand_potion = None
        if Item.player_level <= 5:
            rand_potion = Item.random_item(small_potions)
        elif Item.player_level > 5 and Item.player_level < 10:
            rand_potion = Item.random_item(medium_potions)
        else:
            rand_potion = Item.random_item(large_potions)
        return rand_potion
    
class Spell(Item):
    def __init__(self, player_level):
        self.player_level = player_level
        name, (effect, spell_type) = self.generate_spell()
        self.name, self.effect, self.spell_type = name, effect, spell_type
        self.effect = effect
        self.spell_type = spell_type
        
    def generate_spell(self):
        # Defence (D): Spells cast on player, Offence (O): Spells cast on opponent
        minor_spells = {'Minor Health Spell': (2, 'D'), 'Minor Energy Spell': (2, 'D'), 'Minor Magic Restoration Spell': (2, 'D'),
                        'Minor Damage Spell': (2, 'O'), 'Minor Fatigue Spell': (2, 'O'), 'Minor Magic Drain Spell': (2, 'D')}
        modest_spells = {'Modest Health Spell': (4, 'D'), 'Modest Energy Spell': (4, 'D'), 'Modest Magic Restoration Spell': (4, 'D'),
                        'Modest Damage Spell': (4, 'O'), 'Modest Fatigue Spell': (4, 'O'), 'Modest Magic Drain Spell': (4, 'D')}
        major_spells = {'Major Health Spell': (6, 'D'), 'Major Energy Spell': (6, 'D'), 'Major Magic Restoration Spell': (6, 'D'),
                        'Major Damage Spell': (6, 'O'), 'Major Fatigue Spell': (6, 'O'), 'Major Magic Drain Spell': (6, 'D')}
        rand_spell = None
        if Item.player_level <= 5:
            rand_spell = Item.random_item(minor_spells)
        elif Item.player_level > 5 and Item.player_level < 10:
            rand_spell = Item.random_item(modest_spells)
        else:
            rand_spell = Item.random_item(major_spells)
        return rand_spell