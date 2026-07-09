# Item class
import random

def random_dict_item(dict):
        return random.choice(list(dict.items())) 

class Weapon:
    def __init__(self, player_level):
        self.player_level = player_level
        name, (damage, damage_type) = self.generate_weapon()
        self.name, self.damage, self.damage_type = name, damage, damage_type

    def generate_weapon(self):
        # Dictionary which stores (weapon name: (damage, damage type)) where P = Physical, M = Magical
        low_level_weapons = {'Wood Sword': (2, 'P'), 
                             'Wood Staff': (2, 'M')} 
        med_level_weapons = low_level_weapons | {'Iron Sword': (4, 'P'), 
                                                 'Iron Staff': (4, 'M')}
        high_level_weapons = med_level_weapons | {'Steel Sword': (6, 'P'), 
                                                  'Steel Staff': (6, 'M')}

        weapon_name, weapon_attack = None, None
        if self.player_level <= 5:
            weapon_name, weapon_attack = random_dict_item(low_level_weapons)
        elif self.player_level > 5 and self.player_level < 10:
            weapon_name, weapon_attack = random_dict_item(med_level_weapons)
        else:
            weapon_name, weapon_attack = random_dict_item(high_level_weapons)
        return weapon_name, weapon_attack
    
    def get_name(self):
        return self.name
        
class Armor:
    def __init__(self, player_level):
        self.player_level = player_level
        armor_name, armor_defence = self.generate_armor()
        self.name, self.defence = armor_name, armor_defence

    def generate_armor(self):
        level = self.player_level
        # Dictionary which stores: [armor name: (physical defence, magical defence)]
        low_level_armor = {'Silk Armor': 2} 
        med_level_armor = low_level_armor | {'Iron Armor': 4}
        high_level_armor = med_level_armor | {'Steel Armor': 6}
        armor_name, armor_defence = None, None

        if level <= 5:
            armor_name, armor_defence = random_dict_item(low_level_armor)
        elif level > 5 and level < 10:
            armor_name, armor_defence = random_dict_item(med_level_armor)
        else:
            armor_name, armor_defence = random_dict_item(high_level_armor)
        return armor_name, armor_defence
    
    def get_name(self):
        return self.name
    
class Potion:
    def __init__(self, player_level):
        self.player_level = player_level
        name, (restoration_amount, restoration_type) = self.generate_potion()
        self.name, self.restoration_amount, self.restoration_type = name, restoration_amount, restoration_type

    def generate_potion(self):
        level = self.player_level
        small_potions = {'Small Health Potion': (2, 'H'), 
                         'Small Energy Potion': (2, 'E'), 
                         'Small Magic Potion': (2, 'M')} 
        medium_potions = small_potions | {'Medium Health Potion': (4, 'H'), 
                                          'Medium Energy Potion': (4, 'E'), 
                                          'Medium Magic Potion': (4, 'M')} 
        large_potions = medium_potions | {'Large Health Potion': (6, 'H'), 
                                          'Large Energy Potion': (6, 'E'), 
                                          'Large Magic Potion': (6, 'M')} 
        potion_name, potion_effects = None, None
        if level <= 5:
            potion_name, potion_effects = random_dict_item(small_potions)
        elif level > 5 and level < 10:
            potion_name, potion_effects = random_dict_item(medium_potions)
        else:
            potion_name, potion_effects = random_dict_item(large_potions)
        return potion_name, potion_effects
    
    def get_name(self):
        return self.name
    
class Spell:
    def __init__(self, player_level):
        self.player_level = player_level
        name, (effect, spell_type) = self.generate_spell()
        self.name, self.effect, self.spell_type = name, effect, spell_type
        
    def generate_spell(self):
        level = self.player_level
        # Defence (D): Spells cast on player, Offence (O): Spells cast on opponent
        minor_spells = {'Minor Health Spell': (2, 'D'), 'Minor Energy Spell': (2, 'D'), 
                        'Minor Magic Restoration Spell': (2, 'D'), 'Minor Damage Spell': (2, 'O'), 
                        'Minor Fatigue Spell': (2, 'O'), 'Minor Magic Drain Spell': (2, 'D')}
        modest_spells = minor_spells | {'Modest Health Spell': (4, 'D'), 'Modest Energy Spell': (4, 'D'), 
                                        'Modest Magic Restoration Spell': (4, 'D'), 'Modest Damage Spell': (4, 'O'), 
                                        'Modest Fatigue Spell': (4, 'O'), 'Modest Magic Drain Spell': (4, 'D')}
        major_spells = modest_spells | {'Major Health Spell': (6, 'D'), 'Major Energy Spell': (6, 'D'), 
                                        'Major Magic Restoration Spell': (6, 'D'), 'Major Damage Spell': (6, 'O'), 
                                        'Major Fatigue Spell': (6, 'O'), 'Major Magic Drain Spell': (6, 'D')}
        spell_name, spell_stats = None, None
        if level <= 5:
            spell_name, spell_stats = random_dict_item(minor_spells)
        elif level > 5 and level < 10:
            spell_name, spell_stats = random_dict_item(modest_spells)
        else:
            spell_name, spell_stats = random_dict_item(major_spells)
        return spell_name, spell_stats
    
    def get_name(self):
        return self.name