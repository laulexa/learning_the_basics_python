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
    
create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"])