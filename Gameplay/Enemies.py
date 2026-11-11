# Class for managing enemies as objects
from abc import ABC, abstractmethod

# Interface to outline what every enemy type should have
class Enemy(ABC):
    def __init__(self, damage, damage_type, physical_defence, magical_defence, health):
        self.damage = damage
        self.damage_type = damage_type
        self.physical_defence = physical_defence
        self.magical_defence = magical_defence
        self.health = health

    @abstractmethod
    def attack(self):
        pass

    def take_damage(self, damage_amount):
        self.health -= damage_amount

# Factory for determining the enemy type
def Enemy_factory(kind: str) -> Enemy:
    if kind == "Zombie":
        return Zombie()
    elif kind == "Brigand":
        return Brigand()
    elif kind == "Assassin":
        return Assassin()
    elif kind == "Necromancer":
        return Necromancer()
    elif kind == "Dragon":
        return Dragon()
    else:
        raise ValueError("Unknown enemy type")
    
class Zombie(Enemy):
    def __init__(self):
        super().__init__(2, 'P', 1.25, 1, 5)

    def attack(self):
        print("The Zombie attacks you!")

class Brigand(Enemy):
    def __init__(self):
        super().__init__(4, 'P', 1.25, 0.75, 10)

    def attack(self):
        print("The Brigand strikes at you with their sword!")

class Assassin(Enemy):
    def __init__(self):
        super().__init__(6, 'P', 1, 0.75, 15)

    def attack(self):
        print("The Assassin lunges at you with their daggers!")

class Necromancer(Enemy):
    def __init__(self):
        super().__init__(8, 'M', 1, 0.5, 20)

    def attack(self):
        print("The Necromancer casts a spell on you!")

class Dragon(Enemy):
    def __init__(self):
        super().__init__(2, 'M', 0.5, 1.25, 5)

    def attack(self):
        print("The Dragon blows fire at you!")