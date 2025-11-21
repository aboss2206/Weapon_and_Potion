def main():
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

if __name__ == "__main__":
    main()