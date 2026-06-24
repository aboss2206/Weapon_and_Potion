from Character.Character_Attributes import *
from Gameplay.Encounter_Generation import *
from Character.Inventory import *
from Character.Player_Options import *
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
    player = character_factory(player_class, player_name)

    # Starting game
    game_continue = True
    print("\n-- GAME START --")
    count = 1
    while game_continue:
        # n = random.randint(1, 4)
        n = 2
        encounter = encounter_generator(n)
        if encounter:
            print(f"\n|- Encounter {count} -|")
            if n == 2:
                print(encounter[0])
            else:
                print(encounter)
            print(encounter)
            if n != 1: # 1 == Just Walking
                print('- Your Turn -\nWhat do you wanna do?')
                if n == 2: # Combat encounter
                    combat_encounter(player, encounter[1])
                if n == 3: # Chest
                    chest_encounter(player)
                if n == 4: # Tavern
                    tavern_encounter(player)
            count += 1

            game_continue = input("\nContinue playing? (Enter 'y' or 'n'): ")
            while game_continue not in {'y', 'n'}:
                game_continue = input("Enter 'y' or 'n': ")
            if game_continue == 'n':
                print('\n-- GAME END --\nThanks for playing!\n')
                break
        else:
            continue

if __name__ == "__main__":
    main(test_mode=True)