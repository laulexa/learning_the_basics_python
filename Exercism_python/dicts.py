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
    #print(inventory)
    return inventory

add_items({"coal":1}, ["wood", "iron", "coal", "wood"])

#3

def decrement_items(inventory, items):
    for item in items:
        if item in inventory:
            if inventory[item] > 0:
                inventory[item] -= 1
            else:
                inventory[item] = 0
        
    #print(inventory)
    return inventory

decrement_items({"coal":3, "diamond":1, "iron":1}, ["diamond", "coal", "iron", "iron"])
decrement_items({"iron": 3, "gold": 2}, ["iron", "wood", "iron", "diamond"])

#4
def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    if item in inventory:
        inventory.pop(item, inventory[item])
        #print("inside", inventory)
        return inventory
    #print("outside", inventory)
    return inventory
        
        
remove_item({"coal":2, "wood":1, "diamond":2}, "coal")
remove_item({"iron": 1, "diamond": 2, "gold": 1}, "wood")

#5

def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    my_list = []
    for item in inventory:
        if inventory[item] > 0:
             my_list.append((item, inventory[item])) 
    print(my_list)
    return my_list

list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0})


def list_inventory2(inventory):
    my_list = []
    for item, quantity in inventory.items():
        if quantity > 0:
            my_list.append((item, quantity))
    return my_list