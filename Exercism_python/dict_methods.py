#Exercise 1
def add_item(current_cart, items_to_add):
    updated_cart = current_cart.copy() # I copy the dictionary to safely add or update items in updated_cart,  The original current_cart will stay unchanged. This is important if you need to preserve the original input, especially in functions or tests where you don’t want side effects.
    for item in items_to_add:
        updated_cart[item] = updated_cart.get(item, 0) + 1
    print(updated_cart)
    return updated_cart

#add_item({'Banana': 3, 'Apple': 2, 'Orange': 1}, ('Apple', 'Apple', 'Orange', 'Apple', 'Banana'))
# the reason for creating an updated_cart (a copy of current_cart) is to avoid modifying the original input dictionary
#This changes current_cart directly. So if you reuse the same dictionary elsewhere in your code, its values will be unexpectedly updated. This can cause bugs, especially in bigger programs

def add_item2(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        if item in current_cart:
            current_cart[item] +=1
        else:
            current_cart[item] = 1
    print(current_cart)
    return current_cart

#add_item2({'Banana': 3, 'Apple': 2, 'Orange': 1}, ('Apple', 'Apple', 'Orange', 'Apple', 'Banana'))

#Exercise 2

def read_notes(notes):
    new_dict_notes = dict.fromkeys(notes, 1)
    print(new_dict_notes)
    return new_dict_notes

#read_notes(('Banana','Apple', 'Orange'))

#Exercise 3

def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    for name, ingredients in recipe_updates:
        ideas.update({name: ingredients})
    print(ideas)
    return ideas 
       
#update_recipes({'Banana Bread' : {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1},
#                'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1}},
#                (('Banana Bread', {'Banana': 4,  'Walnuts': 2, 'Flour': 1, 'Butter': 1, 'Milk': 2, 'Eggs': 3}),))
#Exercise 4
def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    sorted_entries = dict(sorted(cart.items()))
    return sorted_entries
#sort_entries({'Banana': 3, 'Apple': 2, 'Orange': 1})
#Exercise 5
#reversed(<dict>.keys()), reversed(<dict>.values()), or reversed(<dict>.items()):
#for item in palette_II.items():

def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    # Step 1: Create the combined fulfillment cart
    fulfillment_cart = {}
    for item, quantity in cart.items():
        aisle, refrigeration = aisle_mapping[item]
        fulfillment_cart[item] = [quantity, aisle, refrigeration]

    # Step 2: Sort it in reverse alphabetical order and return a new dictionary
    return dict(sorted(fulfillment_cart.items(), reverse=True))
send_to_store({'Banana': 3, 'Apple': 2, 'Orange': 1, 'Milk': 2},
                {'Banana': ['Aisle 5', False], 'Apple': ['Aisle 4', False], 'Orange': ['Aisle 4', False], 'Milk': ['Aisle 2', True]})
#Exercise 6

def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    my_updated_inventory = store_inventory.copy()

    for item, order_info in fulfillment_cart.items():
        order_quantity = order_info[0]
        print(order_quantity)
        inventory_info = my_updated_inventory[item]
        print(inventory_info)

        current_quantity = inventory_info[0]
        new_quantity = current_quantity - order_quantity

        if new_quantity == 0:
            my_updated_inventory[item][0] = 'Out of Stock'
        else:
            my_updated_inventory[item][0] = new_quantity
    
    return my_updated_inventory

update_store_inventory({'Orange': [1, 'Aisle 4', False], 'Milk': [2, 'Aisle 2', True], 'Banana': [3, 'Aisle 5', False], 'Apple': [2, 'Aisle 4', False]},
{'Banana': [0, 'Aisle 5', False], 'Apple': [12, 'Aisle 4', False], 'Orange': [1, 'Aisle 4', False], 'Milk': [4, 'Aisle 2', True]})