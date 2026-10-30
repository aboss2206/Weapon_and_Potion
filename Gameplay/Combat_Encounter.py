from Character.Inventory import Inventory
from Gameplay.Encounter_Generation import *
from Gameplay.Enemies import Enemy, Enemy_factory, Zombie, Brigand, Assassin, Dragon

# Functioning for determining the options a player has depending on the type of event they encounter
def combat_encounter(player_traits, player_inventory, enemy_type):
    # Player selects their armor (if they have any)
    if bool(player_inventory.armor):
        print("Select your armor from the following: ")
        for armor_name, quantiy in player_inventory.armor.items():
            print(f"{armor_name} (Defence )")
        armor_choice = input("Select your armor: ")
        while armor_choice not in list(player_inventory.armor.keys()):
            armor_choice = input("Enter a choice from the above list: ")

    enemy = Enemy_factory(enemy_type) # Create enemy object with supplied enemy argument
    while enemy.health != 0 and player_traits.current_health != 0:
        print("\n'p': Physical Attack\n'm': Magical Attack\n'r': Run\n'n': Do nothing")
        player_input = input('Enter choice: ')
        while player_input not in 'pmrn':
            player_input = input("Enter either 'p'(Physical Attack), 'm'(Magical Attack), 'r'(Run), or 'n'(Do nothing): ")
            if player_input == 'p':
                print("Select weapon:")
