from Character.Character_Attributes import *
from Gameplay.Encounter_Generation import *
from Character.Inventory import *

def main():
    '''
    # Intro Greetings
    print('--- Welcome to WEAPON AND POTION! ---')
    response = input('Wanna get the gist of what the game is about? (y or n) ')
    
    # Input Handling
    while response not in 'yn':
        response = input('Sorry I didn\'t catch that, enter either y or n: ')
    if response == 'y':
        print('- Awesome! -')
        print("This game is basically a text-based RPG where your character will make various decisions based on different events that occur\n")

    print("\n- Let's get into Character Creation! -")
    '''
    
    # Creating character
    name = input("Enter your character's name: ")
    print("- Class Selection -")
    print("Pick your class from the following:")
    print("- Warrior (Press h): Medium Strength, Medium Magic, Medium Resilience, Medium Speed, Medium Intelligence")
    print("- Mage (Press e): Low Strength, High Magic, Low Resilience, Medium Speed, High Intelligence")
    print("- Tank (Press o): High Strength, Low Magic, High Resilience, Low Speed, Medium Intelligence")
    player_class = input("Enter h (human), e (elf), or o (orc): ")
    while player_class not in "heo":
        player_class = input("Enter either h, e, or o: ")

    print(f"\nWelcome, {name}!\n")

if __name__ == "__main__":
    main()