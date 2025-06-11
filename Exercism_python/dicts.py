def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    inventory={}
    for item in items:
        if item in inventory: 
            inventory[item] += 1
        else:
            inventory[item] = 1
    print(inventory)
    return inventory

    inventory = {}
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory
    
#create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"])

def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    print(inventory)
    return inventory

add_items({"coal":1}, ["wood", "iron", "coal", "wood"])