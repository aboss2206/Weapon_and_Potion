import random
from Character.Inventory import Inventory
from Character.Character_Attributes import Character
from Items.Item_types import random_dict_item, Weapon, Armor, Potion, Spell

# Chest function takes the player's inventory and updates it with a randomly generated item or amount of gold
def chest(player_inventory, player_traits):
    player_level = player_traits.level # Checking player's level
    n = random.randrange(1, 6) # n1 represents the type e.g. armor, gold
    # Item
    if n != 5: 
        new_item = None
        if n == 1: # Weapon
            new_item = Weapon(player_level) # Generate item
        elif n == 2: # Armor
            new_item = Armor(player_level)     
        elif n == 3: # Potion
            new_item = Potion(player_level)
        else: # Spell
            new_item = Spell(player_level)
        player_inventory.update_inventory(new_item) # Updating inventory
        return new_item
    # Gold
    else: 
        gold_amount = random.randrange(1, 20) # Random amount of gold
        player_inventory.deposit_gold(gold_amount) 
        return f"{gold_amount} Gold"