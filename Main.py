from Character.Character_Setup import *
from Gameplay.Encounter_Generation import *

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
    print("- Race Selection -")
    print("Pick your race from the following:")
    print("- HUMAN (Press h): Medium Strength, Medium Magic, Medium Resilience, Medium Speed, Medium Intelligence")
    print("- ELF (Press e): Low Strength, High Magic, Low Resilience, Medium Speed, High Intelligence")
    print("- ORC (Press o): High Strength, Low Magic, High Resilience, Low Speed, Medium Intelligence")
    race = input("Enter h (human), e (elf), or o (orc): ")
    while race not in "heo":
        race = input("Enter either h, e, or o: ")

    # Saving info to character class
    if race == "h":
        Character(name, race, 20, 20, 20, 20, 20, 20, 0)
    elif race == "e":
        Character(name, race, 10, 30, 10, 20, 30, 20, 0)
    else:
        Character(name, race, 30, 10, 30, 10, 20, 20, 0)

    print(f"\nWelcome, {name}!\n")

if __name__ == "__main__":
    main()