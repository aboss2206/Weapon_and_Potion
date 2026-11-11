# Dataclass to hold info about character like inventory and health
from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Character(ABC):
    def __init__(self):
        self.level, self.level_xp, self.level_up_threshold = 1, 0, 10
        self.resistance, self.resistance_xp, self.resistance_threshold = 0, 0, 0
        self.strength, self.strength_xp, self.strength_threshold = 0, 0, 0
        self.magic, self.magic_xp, self.magic_threshold = 0, 0, 0
        self.health = 0
        self.current_health = self.health
        self.character_class = "Not defined"
        self.kill_count = 0
        self.encounter_count = 0

    # Method for adding xp to a certain skill
    def add_xp(self, skill, xp_amount):
        excess_xp = 0
        if skill == "strength":
            new_xp_amount = self.strength_xp + xp_amount # Current + new xp
            if new_xp_amount > self.strength_threshold: # Checking if the player can level up
                excess_xp = new_xp_amount - self.strength_threshold # The amount of extra xp that would go towards next level
                self.skill_level_up(skill)
            self.strength_xp = excess_xp # Excess xp is added to new level
        elif skill == "resistance":
            new_xp_amount = self.resistance_xp + xp_amount 
            if new_xp_amount > self.resistance_threshold: 
                excess_xp = new_xp_amount - self.resistance_threshold 
                self.skill_level_up(skill)
            self.resistance_xp = excess_xp
        else:
            new_xp_amount = self.magic_xp + xp_amount 
            if new_xp_amount > self.magic_threshold: 
                excess_xp = new_xp_amount - self.magic_threshold 
                self.skill_level_up(skill)
            self.magic_xp = excess_xp 

    # Method for leveling up main level
    def level_up(self): 
        self.level += 1
        self.level_xp = 0
        self.level_up_threshold += 1

    # Method for skill level increasing
    def skill_level_up(self, skill): # skill = strength, resistance, or magic
        if skill == "strength":
            self.strength += 1
            self.strength_xp = 0
            self.strength_threshold += 1
        elif skill == "resistance":
            self.resistance += 1
            self.resistance_xp = 0
            self.resistance_threshold += 1
        else:
            self.magic += 1
            self.magic_xp = 0
            self.magic_threshold += 1

    # Method for taking damage
    def take_damage(self, damage, damage_type, equipped_armor):
        resistance_divisor = 1 + (self.resistance / 10)
        if damage_type == 'P':
            armor_divisor = 1 + (equipped_armor.physical_defence / 10)
        else:
            armor_divisor = 1 + (equipped_armor.magical_defence / 10)
        self.current_health -= (damage / (resistance_divisor * armor_divisor)) # Factors in player's resistance
        self.add_xp("resistance", 3) # Player gets some resistance xp for taking a hit
    
    # Method for player death
    def player_death(self):
        if self.level[1] > 0:
            print("XP reset")
            self.level[1] = 0
        if self.level[0] > 0:
            print("Level decreased by 1")
            self.level[1] -= 1
            self.level[2] -= 1 # Threshold for leveling reduced to match previous level

    # Method for displaying character stats
    def show_stats(self):
        print('-----------')
        print(f'Name: {self.name}')
        print(f'Class: {self.character_class}')
        print(f'Level: {self.level}')
        print(f"Resistance: {self.resistance}")
        print(f"Strength: {self.strength}")
        print(f"Magic: {self.magic}")
        print(f"Encounters: {self.encounter_count}")
        print(f"Kill Count: {self.kill_count}")
        print('-----------')

# Factory for determining class
def character_factory(class_choice: str, name: str) -> Character:
    if class_choice == "Warrior":
        return Warrior(name)
    elif class_choice == "Magician":
        return Magician(name)
    elif class_choice == "Tank":
        return Tank(name)
    else:
        return None

# Derived classes for each character class
class Warrior(Character):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.character_class = "Warrior"
        self.health = 100
        self.current_health = self.health
        self.resistance = 15
        self.strength = 20
        self.magic = 10
    
class Magician(Character):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.character_class = "Magician"
        self.health = 90
        self.current_health = self.health
        self.resistance = 15
        self.strength = 10
        self.magic = 20
    
class Tank(Character):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.character_class = "Warrior"
        self.health = 110
        self.current_health = self.health
        self.resistance = 20
        self.strength = 15
        self.magic = 10