import random

# Function that uses a random number generator to determine what type of encounter the character will have
def encounter_generator():
    n = random.randint(1, 5)
    event = None
    # Event 1: Just Walking
    if n == 1:
        event = "Walking..."
    # Event 2: Encountered an enemy
    

# A separate function for determining the type of enemy the player will encounter
def enemy_encounter_generator():
    n = random.randint(1, 5)
    enemy_type = None
    if n == 1:
        enemy_type = "Necromancer"
    elif n == 2:
        enemy_type = "Bandit"
    elif n == 3:
        enemy_type = "Dragon"
    elif n == 4:
        enemy_type = "Zombie" 
    else:
        enemy_type = "Assassin"
    return enemy_type