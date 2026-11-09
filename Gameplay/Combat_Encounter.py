from Character.Inventory import Inventory
from Gameplay.Encounter_Generation import *
from Gameplay.Enemies import Enemy, Enemy_factory, Zombie, Brigand, Assassin, Dragon

# Functioning for determining the options a player has depending on the type of event they encounter
def combat_encounter(player_traits, player_inventory, enemy_type):
    # Player selects their armor (if they have any)
    player_armors = player_inventory.get_armor()
    player_input = ""
    equipped_armor = None
    if player_armors:
        print("Select your armor from the following: ")
        for armor in player_armors:
            print(f"{armor.name} (Physical Defence: {armor.physical_defence}, Magical Defence: {armor.magical_defence})")
        player_input = input("Select your armor: ")
        while player_input not in [armor.name for armor in player_armors]:
            player_input = input("Enter a choice from the above list: ")
        for armor in player_armors:
            if player_input == armor.name:
                equipped_armor = armor
        print("\n----------------------------")
        print(f"{equipped_armor.name} has been equipped.")
        print("----------------------------")
    else:
        player_input = input("Shit, you don't have any armor yet, still wanna fight? (y or n): ")
        while player_input not in "yn":
            player_input = input("Enter 'y' or 'n': ")
        if player_input == 'y':
            print("\n---------------")
            print("Hell yeah, who needs armor anyway?")
            print("---------------")
        else:
            print("\nYeah, no armor is kinda risky")
            return

    # Player selects their weapon (if they have any)
    player_weapons = player_inventory.get_weapons()
    equipped_weapon = None
    if player_weapons:
        print("Select your weapons from the following: ")
        for weapon in player_weapons:
            print(f"{weapon.name} (Physical Defence: {weapon.physical_defence}, Magical Defence: {weapon.magical_defence})")
        player_input = input("Select your weapon: ")
        while player_input not in [weapon.name for weapon in player_weapons]:
            player_input = input("Enter a choice from the above list: ")
        for weapon in player_weapons:
            if player_input == weapon.name:
                equipped_weapon = weapon
        print("\n----------------------------")
        print(f"{equipped_weapon.name} has been equipped.")
        print("----------------------------")
    else:
        player_input = input("\nShit, you don't have any weapons yet, still wanna fight? (y or n): ")
        while player_input not in "yn":
            player_input = input("Enter 'y' or 'n': ")
        if player_input == "y":
            print("\n---------------")
            print("Hell yeah, weapons are overrated!")
            print("---------------")
        else:
            print("\nYeah, no weapons is kinda risky")

    enemy = Enemy_factory(enemy_type) # Create enemy object with supplied enemy argument

    # Combat
    while True:
        # Player Turn
        print("\n-----------")
        print("Your Turn")
        print("-----------")
        print("\n'a': Attack\n'r': Run")
        player_input = input('Enter choice: ')
        while player_input not in 'ar':
            player_input = input("Enter either 'a'(Attack) or 'r'(Run): ")
        if player_input == "p":
            applied_damage = 0
            # Checking if equipped weapon does physical or magical damage
            if equipped_weapon.damage_type == 'P':
                applied_damage = equipped_weapon.damage * enemy.physical_defence
                enemy.take_damage(applied_damage) # Reduce enemy health by amount of physical damage multiplied by physical defence
                print(f"{applied_damage} physical damage applied to {enemy_type}!")
                # Player gets xp
            else:
                applied_damage = equipped_weapon.damage * enemy.magical_defence
                enemy.take_damage(applied_damage)
                print(f"{applied_damage} magical damage applied to {enemy_type}!")
        # Check if enemy died after player turn
        if enemy.health <= 0:
            print("\n----------------------")
            print(f"Hell yeah! the {enemy_type} is dead!")
            print("----------------------\n")
            break

        # Enemy Turn
        print("\n-----------")
        print("Their Turn")
        print("-----------\n")
        enemy.attack()
        print()
        player_traits.take_damage(enemy.damage) # Resistance is factored in the function
        print(f"Shit, you took {enemy.damage} damage!")
        # Check if player died after enemy turn
        if player_traits.current_health <= 0:
            player_traits.player_death()
            print("\n----------------")
            print(f"Shit, you died!")
            print("------------------\n")
            print("- Level decreased by 1")
            print("- Level xp reset")
            break