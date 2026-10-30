from Character.Character_Attributes import Character, character_factory, Warrior, Magician, Tank
from Gameplay.Encounter_Generation import encounter_generator, enemy_encounter_generator
from Character.Inventory import Inventory
from Gameplay.Combat_Encounter import combat_encounter
from Items.Chest import chest
from Items.Item_types import Weapon, Armor, Potion, Spell
import random

def main(test_mode=False):
    if test_mode:
        player_name, player_class = "Alex", "Warrior"
    else:
        # Intro Greetings
        print('--- Welcome to WEAPON AND POTION! ---')
        response = input('Wanna get the gist of what the game is about? (y or n): ')
    
        # Input Handling
        while response not in 'yn':
            response = input('Sorry I didn\'t catch that, enter either \'y\' or \'n\': ')
        if response == 'y':
            print('\n- Awesome! -')
            print("This game is basically a text-based RPG where your character will make various decisions based on different events that occur\n")

        print("\n- Let's get into Character Creation! -")
    
        # Getting character name
        player_name = input("Enter your character's name: ")
        print(f'\nWelcome, {player_name}!\n')

        # Getting character class
        print("- Class Selection -")
        print("Pick your class from the following:")
        print("- Warrior (Press w): Medium Resistance, High Endurance, Low Magic")
        print("- Magician (Press m): Low Resistance, Medium Endurance, High Magic")
        print("- Tank (Press t): High Resistance, Medium Endurance, Low Magic")
        class_choice = input("Enter class: ")
        player_class = None
        while class_choice not in "wmt":
            class_choice = input("Enter either w, m, or t: ")
        print('\n- Summary -')
        print(f'Your name is {player_name}!')
        if class_choice == 'w':
            player_class = "Warrior"
            print("You're a Willful Warrior!")
        elif class_choice == "m":
            player_class = "Magician"
            print("You're a Majestic Magician!")
        else:
            player_class = "Tank"
            print("You're a Tough Tank!")

    # Initialising player traits and inventory
    player_traits = character_factory(player_class, player_name)
    player_inventory = Inventory()

    # Starting game
    print('\n-----------------------------------------')
    print("--------       GAME START       ---------")
    print("-----------------------------------------")
    count = 0
    player_response = None
    while True:
        # Generating and printing encounter
        n = random.choice([1, 3, 4]) #random.randint(1, 4)
        encounter = encounter_generator(n)
        if n != 1:
            player_traits.encounter_count += 1
            print("\n-----------")
            print(f"Encounter {player_traits.encounter_count}")
            print("-----------")
        else:
            print('\n-----------')
        print(encounter)
        print('-----------')
        print('Your Options:')
        # Walking
        if n == 1: 
            print("\'c\': continue, \'s\': check stats, \'q\': quit")
            player_response = input("Enter option: ")
            while player_response not in "csq":
                player_response = input("Enter either \'s\'(check stats) or \'q\'(quit): ")
            if player_response == 'c':
                print("-----------")
                print('A few moments later...')
                print("-----------")
            if player_response == 's':
                print("-----------")
                print('Your Stats')
                player_traits.show_stats()
            elif player_response == 'q':
                break
        # Enemy
        elif n == 2:
            print("\'f\': fight, \'r\': run, \'q\': quit")
            player_response = input("Enter option: ")
            while player_response not in "frq":
                player_response = input("Enter either \'f\'(fight), \'r\'(run) or \'q\'(quit): ")
            if player_response == 'f':
                print("-- FIGHT TIME --")
                if "Necromancer" in encounter:
                    enemy_type = "Necromancer"
                elif "Brigand" in encounter:
                    enemy_type = "Brigand"
                elif "Dragon" in encounter:
                    enemy_type = "Dragon"
                elif "Zombie" in encounter:
                    enemy_type = "Zombie"
                else:
                    enemy_type = "Assassin"
                combat_encounter(player_traits, player_inventory, enemy_type)
        # Chest
        elif n == 3:
                print("\'o\': open, \'l': leave it, \'q\': quit")
                player_response = input("Enter option: ")
                while player_response not in "olq":
                    player_response = input("Enter either \'o\'(open chest), \'l\'(leave chest) or \'q\'(quit): ")
                if player_response == 'o':
                    new_item = chest(player_inventory, player_traits)
                    if isinstance(new_item, Weapon) or isinstance(new_item, Armor) or isinstance(new_item, Potion) or isinstance(new_item, Spell):
                        print("-----------")
                        print(f"NEW ITEM: {new_item.get_name()}")
                        print("-----------")
                    else: # Gold
                        print("-----------")
                        print(f"NEW ITEM: {new_item}")
                        print("-----------")
                elif player_response == 'l':
                    print("-----------")
                    print("Yeah, f#!@ that chest.")
                    print("-----------")
                else:
                    break
        # Tavern
        else:
            print("\'r\': rest (10 Gold), \'c\': continue, \'q\': quit")
            player_response = input("Enter option: ")
            while player_response not in "rcq":
                player_response = input("Enter either \'r\'(rest), \'c\'(continue) or \'q\'(quit): ")
            while player_response == 'r' and player_inventory.gold < 10:
                print("-----------")
                player_response = input(f"Insufficient gold (You have {player_inventory.get_gold()} gold), enter another option: ")
            if player_response == 'r':
                if player_traits.current_health == player_traits.health:
                    print("-----------")
                    player_response = input(f"Are you sure? Your health is full so it won't do shit (y or n): ")
                    if player_response == 'y':
                        print("-----------")
                        print("You take a well-deserved, arguably unnecessary, break!")
                        print("-----------")
                    else:
                        print("-----------")
                        print("Good idea, maybe later")
                        print("-----------")
                else:
                    player_inventory.withdraw_gold(10)
                    print("-----------")
                    print("Health fully restored!")
                    print("-----------")
            elif player_response == 'c':
                print("-----------")
                print("Yeah, taverns are overrated")
                print("-----------")
            else:
                break

    print('\n-----------------------------------------')
    print("------     THANKS FOR PLAYING!   --------")
    print("-----------------------------------------\n")
    print('Final Stats')
    player_traits.show_stats()

if __name__ == "__main__":
    main(test_mode=True)