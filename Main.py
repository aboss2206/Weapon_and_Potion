from Character.Character_Attributes import Character, character_factory, Warrior, Magician, Tank
from Gameplay.Encounter_Generation import encounter_generator, enemy_encounter_generator
from Items.Inventory import Inventory
from Gameplay.Combat_Encounter import combat_encounter, chest_encounter
from Items.Chest import *

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
    print("-----------------------------------------\n")
    count = 1
    player_response = None
    while True:
        # Generating and printing encounter
        n = 1
        encounter = encounter_generator(n)
        print(encounter)
        print('\n------------')
        print('Your Options')
        print('------------')
        # Walking
        if n == 1: 
            print("\'s\': check stats, \'q\': quit")
            player_response = input("Enter option: ")
            while player_response not in "sq":
                player_response = input("Enter either \'s\'(check stats) or \'q\'(quit): ")
            if player_response == 's':
                print()
                print('Your Stats')
                player_traits.show_stats()
                print()
            elif player_response == 'q':
                break
        # Chest
        elif n == 3:
            print("\'o\': open, \'w\': leave it, \'q\': quit")
            player_response = input("Enter option: ")
            while player_response not in "owq":
                player_response = input("Enter either \'o\'(open chest), \'l\'(leave chest) or \'q\'(quit): ")
            if player_response == 'o':
                print()
            

    print('\n-----------------------------------------')
    print("------     THANKS FOR PLAYING!   --------")
    print("-----------------------------------------\n")
    print('Final Stats')
    player_traits.show_stats()

if __name__ == "__main__":
    main(test_mode=True)