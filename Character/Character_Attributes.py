# Dataclass to hold info about character like inventory and health
from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Character(ABC):
    character_class: str
    name: str 
    total_health: int
    current_health: int # For combat

    @property
    def level(self) -> list[int]: # List containing [Current level, level_xp, threshold to level up]
        return [0, 0, 10]
    
    @property
    @abstractmethod
    def resistance(self) -> list[int]:
        pass

    @property
    @abstractmethod
    def strength(self) -> list[int]:
        pass
    
    @property
    @abstractmethod
    def magic(self) -> list[int]:
        pass

    # Method for adding xp to a certain skill
    def add_xp(self, skill, xp_amount):
        new_xp_amount = self.skill[1] + xp_amount # Current + new xp
        if new_xp_amount > self.skill[2]: # Checking if the player can level up
            self.level_up(skill)
            excess_xp = new_xp_amount - self.skill[2] # The amount of extra xp that would go towards next level
            self.skill[1] = excess_xp # Excess xp is added to new level

    # Method for leveling up main level and skills
    def level_up(self, skill_or_level): # Skill can be either
        self.skill_or_level[0] += 1 # current level increases
        self.skill_or_level[1] = 0 # xp reset to 0
        self.skill_or_level[2] += 1 # xp threshold for next level increases

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

# Factory for determining class
def character_factory(class_choice: str, name: str) -> Character:
    if class_choice == "Warrior":
        return Warrior(class_choice, name, total_health=100, current_health=100)
    elif class_choice == "Magician":
        return Magician(class_choice, name, total_health=90, current_health=90)
    elif class_choice == "Tank":
        return Tank(class_choice, name, total_health=110, current_health=110)
    else:
        return None

# Derived classes for each race
class Warrior(Character):
    @property
    def resistance(self) -> list[int]:
        return [15, 0, 5]
    
    @property
    def strength(self) -> list[int]:
        return [20, 0, 5]
    
    @property
    def magic(self) -> list[int]:
        return [10, 0, 5]
    
class Magician(Character):
    @property
    def resistance() -> list[int]:
        return [15, 0, 5]
    
    @property
    def strength(self) -> list[int]:
        return [10, 0, 5]
    
    @property
    def magic(self) -> list[int]:
        return [20, 0, 5]
    
class Tank(Character):
    @property
    def resistance() -> list[int]:
        return [20, 0, 5]
    
    @property
    def strength(self) -> list[int]:
        return [15, 0, 5]
    
    @property
    def magic(self) -> list[int]:
        return [10, 0, 5]