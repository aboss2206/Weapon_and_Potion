# Class for managing enemies as objects
from abc import ABC, abstractmethod

# Interface to outline what every enemy type should have
class Enemy(ABC):
    @property
    @abstractmethod
    def health(self) -> int:
        pass

    @property
    @abstractmethod
    def damage(self) -> int:
        pass

    @abstractmethod
    def encounter(self):
        pass

    @abstractmethod
    def attack(self):
        pass

    def take_damage(self, damage_amount):
        self.health -= damage_amount

# Factory for determining the enemy type
def Enemy_factory(kind: str) -> Enemy:
    if kind == "Zombie":
        return Zombie()
    elif kind == "Bandit":
        return Bandit()
    elif kind == "Assassin":
        return Assassin()
    elif kind == "Necromancer":
        return Necromancer()
    elif kind == "Dragon":
        return Dragon()
    else:
        print("Unknown enemy type")
    
class Zombie(Enemy):
    def health() -> int:
        return 5
    
    def damage() -> int:
        return 2

    def encounter(self):
        print("A Zombie drags itself into view!")

    def attack(self):
        print("The Zombie attacks you!")

class Bandit(Enemy):
    def health() -> int:
        return 10
    
    def damage() -> int:
        return 4

    def encounter(self):
        print("A Bandit, with a battle cry, blocks your path!")

    def attack(self):
        print("The Bandit strikes at you with their sword!")

class Assassin(Enemy):
    def health() -> int:
        return 15

    def damage() -> int:
        return 6

    def encounter(self):
        print("An Assassin flips into view from around the corner")

    def attack(self):
        print("The Assassin lunges at you with their daggers!")

class Necromancer(Enemy):
    def health() -> int:
        return 20
    
    def damage() -> int:
        return 8

    def encounter(self):
        print("A figure steps through a portal created in front of you. It's a Necromancer!")

    def attack(self):
        print("The Necromancer casts a spell on you!")

class Dragon(Enemy):
    def health() -> int:
        return 30
    
    def damage() -> int:
        return 12

    def encounter(self):
        print("A Dragon flies into view!")

    def attack(self):
        print("The Dragon blows fire at you!")