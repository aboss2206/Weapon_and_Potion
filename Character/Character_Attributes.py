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

    # Method for adding xp to a certain skill
    def add_xp(self, skill, xp_amount):
        new_xp_amount = self.skill[1] + xp_amount # Current + new xp
        if new_xp_amount > self.skill[2]: # Checking if the player can level up
            self.level_up(skill)
            excess_xp = new_xp_amount - self.skill[2] # The amount of extra xp that would go towards next level
            self.skill[1] = excess_xp # Excess xp is added to new level

    # Method for leveling up main level and skills
    def level_up(self, skill_or_level): # Skill can be either
        self.skill_or_level += 1 # current level increases
        self.skill_or_level = 0 # xp reset to 0
        self.skill_or_level += 1 # xp threshold for next level increases

    # Method for taking damage
    def take_damage(self, damage):
        self.current_health -= (damage - (self.resistance / 10)) # Factors in player's resistance

    # Method for dealing physical attacks
    def physical_attack(self, damage):
        return damage + (self.strength / 10)

    # Method for dealing magical attacks
    def magical_attack(self, damage):
        return damage + (self.strength / 10)
    
    # Method for player death
    def player_death(self):
        print("Oh s?!#, you died!")
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