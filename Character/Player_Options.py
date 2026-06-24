from Gameplay.Encounter_Generation import *
from Gameplay.Enemies import *

# Functioning for determining the options a player has depending on the type of event they encounter
def combat_encounter(player, enemy_type):
    enemy = Enemy_factory(enemy_type) # Create enemy object with supplied enemy argument
    while enemy.health != 0 and player.current_health != 0:
        print("\n'p': Physical Attack\n'm': Magical Attack\n'r': Run\n'c': Chill")
        player_input = input('Enter choice: ')
        while player_input not in 'arc':
            player_input = input("Enter either 'p'(Physical Attack), 'm'(Magical Attack), 'r'(Run), or 'c'(Chill): ")

def chest_encounter(player):
    print("\n'o': Open it\n'l': Leave it")
    player_input = input('Enter choice: ')
    while player_input not in 'ol':
        player_input = input("Enter either 'o'(Open it) or 'l'(Leave it): ")
    print('Cool!')

def tavern_encounter(player):
    print("\n'r': Rest\n'c': Continue")
    player_input = input('Enter choice: ')
    while player_input not in 'rc':
        player_input = input("Enter either 'r'(Rest) or 'c'(Continue): ")
    print('Cool!')   