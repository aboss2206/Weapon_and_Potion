# Dataclass to hold info about character
from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Character(ABC):
    character_class: str
    name: str 

    @property
    def level(self) -> list[int]: # List containing [Current level, level_xp, threshold to level up]
        return [0, 0, 10]
    
    @property
    @abstractmethod
    def resistance(self) -> list[int]:
        pass

    @property
    @abstractmethod
    def endurance(self) -> list[int]:
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
    def level_up(self, skill): 
        self.skill[0] += 1 # current level increases
        self.skill[1] = 0 # xp reset to 0
        self.skill[2] += 1 # xp threshold for next level increases

    # Method for taking damage

# Factory for determining class
def character_factory(class_choice: str, name: str) -> Character:
    if class_choice == "Warrior":
        return Warrior(class_choice, name)
    elif class_choice == "Magician":
        return Magician(class_choice, name)
    elif class_choice == "Tank":
        return Tank(class_choice, name)
    else:
        return None

# Derived classes for each race
class Warrior(Character):
    @property
    def resistance() -> list[int]:
        return [15, 0, 5]
    
    @property
    def endurance(self) -> list[int]:
        return [20, 0, 5]
    
    @property
    def magic(self) -> list[int]:
        return [10, 0, 5]
    
class Magician(Character):
    @property
    def resistance() -> list[int]:
        return [10, 0, 5]
    
    @property
    def endurance(self) -> list[int]:
        return [15, 0, 5]
    
    @property
    def magic(self) -> list[int]:
        return [20, 0, 5]
    
class Tank(Character):
    @property
    def resistance() -> list[int]:
        return [20, 0, 5]
    
    @property
    def endurance(self) -> list[int]:
        return [15, 0, 5]
    
    @property
    def magic(self) -> list[int]:
        return [10, 0, 5]