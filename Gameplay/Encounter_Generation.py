import random

# Function that uses a random number generator to determine what type of encounter the character will have
def encounter_generator(n):
    event = None
    # Event 1: Just Walking
    if n == 1:
        event = "Walking..."
        event_label = "Walking"
    # Event 2: Encountered an enemy
    elif n == 2:
        enemy_type = enemy_encounter_generator()
        # Checking if enemy label starts with noun:
        if enemy_type[0] in "AEIOU":
            event = f"Oh no! You've encountered an {enemy_type}! What do you want to do?"
        else:
            event = f"Oh no! You've encountered a {enemy_type}! What do you want to do?"
        return event, enemy_type
    # Event 3: Found a chest
    elif n == 3: 
        event = "You found a chest! Wanna open it?"
    elif n == 4: # Event 4: Found a tavern
        event = "You found a tavern! Would you like to rest here? (Costs 10 Gold)"
    return event

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