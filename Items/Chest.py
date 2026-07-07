import random
from Items.Inventory import Inventory
from Character.Character_Attributes import Character
from Items.Item_types import random_dict_item, Weapon, Armor, Potion, Spell

# Chest function takes the player's inventory and updates it with a randomly generated item or amount of gold
def chest(player_inventory, player_traits):
    player_level = player_traits.level # Checking player's level
    n = random.randrange(1, 6) # n1 represents the type e.g. armor, gold
    if n == 1: # Weapon
        new_weapon = Weapon(player_level) # Generate item
        player_inventory.update_inventory(new_weapon) # Updating inventory
    elif n == 2: # Armor
        new_armor = Armor(player_level)
        player_inventory.update_inventory(new_armor) 
    elif n == 3: # Potion
        new_potion = Potion(player_level)
        player_inventory.update_inventory(new_potion) 
    elif n == 4: # Spell
        new_spell = Spell(player_level)
        player_inventory.update_inventory(new_spell) 
    else: # Gold
        gold_amount = random.randrange(1, 20) # Random amount of gold
        player_inventory.deposit_gold(gold_amount) 