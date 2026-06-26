from Gameplay.Encounter_Generation import *
import random

# random.seed(42)

for i in range(10):
    n = random.randrange(1, 5)
    encounter = encounter_generator(n)
    print(encounter)

