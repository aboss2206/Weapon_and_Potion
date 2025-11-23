# Dataclass to hold info about character
from dataclasses import dataclass

@dataclass
class Character:
    name: str
    race: str
    strength: int
    magic: int
    resilience: int
    speed: int
    intelligence: int