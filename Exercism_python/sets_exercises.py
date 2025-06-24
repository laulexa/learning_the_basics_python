# pylint: disable-all
# flake8: noqa,
from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)
#Exercise 1
def clean_ingredients(dish_name, dish_ingredients):
    set_dish_ingredients = set(dish_ingredients)
    #print(set_dish_ingredients)
    #print(type(set_dish_ingredients))
    clean_tuple = (dish_name, set_dish_ingredients)
    print(clean_tuple)
    return clean_tuple

#clean_ingredients('Punjabi-Style Chole', ['onions', 'tomatoes', 'ginger paste', 'garlic paste', 'ginger paste', 'vegetable oil', 'bay leaves', 'cloves', 'cardamom', 'cilantro', 'peppercorns', 'cumin powder', 'chickpeas', 'coriander powder', 'red chili powder', 'ground turmeric', 'garam masala', 'chickpeas', 'ginger', 'cilantro'])

#better solution
def clean_ingredients2(dish_name, dish_ingredients):
    """Remove duplicates from `dish_ingredients`.

    :param dish_name: str - containing the dish name.
    :param dish_ingredients: list - dish ingredients.
    :return: tuple - containing (dish_name, ingredient set).

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    """
    return dish_name, set(dish_ingredients)

#clean_ingredients2('Punjabi-Style Chole', ['onions', 'tomatoes', 'ginger paste', 'garlic paste', 'ginger paste', 'vegetable oil', 'bay leaves', 'cloves', 'cardamom', 'cilantro', 'peppercorns', 'cumin powder', 'chickpeas', 'coriander powder', 'red chili powder', 'ground turmeric', 'garam masala', 'chickpeas', 'ginger', 'cilantro'])

#exercise 2
def check_drinks(drink_name, drink_ingredients):
    """Append "Cocktail" (alcohol)  or "Mocktail" (no alcohol) to `drink_name`, based on `drink_ingredients`.

    :param drink_name: str - name of the drink.
    :param drink_ingredients: list - ingredients in the drink.
    :return: str - drink_name appended with "Mocktail" or "Cocktail".

    The function should return the name of the drink followed by "Mocktail" (non-alcoholic) and drink
    name followed by "Cocktail" (includes alcohol).

    """
    for item in drink_ingredients:
        #print(item)
        if item in ALCOHOLS:
            alcoholic = drink_name + " Cocktail"
            print(alcoholic)
            return alcoholic
    non_alcoholic  = drink_name + " Mocktail"
    print(non_alcoholic)
    return non_alcoholic

#check_drinks('Honeydew Cucumber', ['honeydew', 'coconut water', 'mint leaves', 'lime juice', 'salt', 'english cucumber'])
#check_drinks('Shirley Tonic', ['cinnamon stick', 'scotch', 'whole cloves', 'ginger', 'pomegranate juice', 'sugar', 'club soda'])

#Exercise 3
def categorize_dish(dish_name, dish_ingredients):
    """Categorize `dish_name` based on `dish_ingredients`.

    :param dish_name: str - dish to be categorized.
    :param dish_ingredients: set - ingredients for the dish.
    :return: str - the dish name appended with ": <CATEGORY>".

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    `<CATEGORY>` can be any one of  (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    All dishes will "fit" into one of the categories imported from `sets_categories_data.py`

    """
    if dish_ingredients.issubset(VEGAN):
        print("VEGAN")
        return dish_name + ":" + " VEGAN"
    elif dish_ingredients.issubset(VEGETARIAN):
        print("VEGETARIAN")
        return dish_name + ":" + " VEGETARIAN"
    elif dish_ingredients.issubset(KETO):
        print("KETO")
        return dish_name + ":" + " KETO"
    elif dish_ingredients.issubset(PALEO):
        print("PALEO")
        return dish_name + ":" + " PALEO" 
    else: 
        print("OMNIVORE")
        return dish_name + ":" + " OMNIVORE"

#categorize_dish('Sticky Lemon Tofu', {'tofu', 'soy sauce', 'salt', 'black pepper', 'cornstarch', 'vegetable oil', 'garlic', 'ginger', 'water', 'vegetable stock', 'lemon juice', 'lemon zest', 'sugar'})
#categorize_dish('Shrimp Bacon and Crispy Chickpea Tacos with Salsa de Guacamole', {'shrimp', 'bacon', 'avocado', 'chickpeas', 'fresh tortillas', 'sea salt', 'guajillo chile', 'slivered almonds', 'olive oil', 'butter', 'black pepper', 'garlic', 'onion'})

#Exercise 4

def tag_special_ingredients(dish):
    """Compare `dish` ingredients to `SPECIAL_INGREDIENTS`.

    :param dish: tuple - of (dish name, list of dish ingredients).
    :return: tuple - containing (dish name, dish special ingredients).

    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `sets_categories_data.py`.
    """
    #My Solution
    #special = set(dish[1]) & SPECIAL_INGREDIENTS
    #print(dish[0], special)
    #return(dish[0], special)

    #Improved
    name, ingredients = dish
    special = set(ingredients) & SPECIAL_INGREDIENTS
    print(name,special)
    return(name, special)


#tag_special_ingredients(('Ginger Glazed Tofu Cutlets', ['tofu', 'soy sauce', 'ginger', 'corn starch', 'garlic', 'brown sugar', 'sesame seeds', 'lemon juice']))
#tag_special_ingredients(('Arugula and Roasted Pork Salad', ['pork tenderloin', 'arugula', 'pears', 'blue cheese', 'pine nuts', 'balsamic vinegar', 'onions', 'black pepper']))

'''
his tuple contains:
A string (dish name) ✅ hashable
A list (ingredients) ❌ not hashable
Python's set() constructor only works with hashable elements, and lists are not hashable, so you get a TypeError.

set(dish) fails because dish[1] is a list (not hashable).
Extract the list first: ingredients = dish[1]
Then do set(ingredients) & SPECIAL_INGREDIENTS
'''

#Exercise 5
def compile_ingredients(dishes):
    """Create a master list of ingredients.

    :param dishes: list - of dish ingredient sets.
    :return: set - of ingredients compiled from `dishes`.

    This function should return a `set` of all ingredients from all listed dishes.
    """

    ingredients_compiled = set()
    for dish in dishes:
        ingredients_compiled |= dish
    return ingredients_compiled
    
#compile_ingredients([ {'tofu', 'soy sauce', 'ginger', 'corn starch', 'garlic', 'brown sugar', 'sesame seeds', 'lemon juice'},
 #          {'pork tenderloin', 'arugula', 'pears', 'blue cheese', 'pine nuts',
  #         'balsamic vinegar', 'onions', 'black pepper'},
   #        {'honeydew', 'coconut water', 'mint leaves', 'lime juice', 'salt', 'english cucumber'}])

"""
You're on the right track with using set union (|), but your current approach assumes there are exactly three dishes, 
which is not safe or generalizable — and it will cause an IndexError if the list has fewer than 3 items
"""

''' print(dishes)
    print(type(dishes))
    print('1', type(dishes[0]))
    print('2', type(dishes[1]))
    print('3', type(dishes[2]))

    ingredients_compiled = dishes[0] | dishes[1] | dishes[2]
    print(ingredients_compiled)
    return ingredients_compiled'''

#exercise #6
def separate_appetizers(dishes, appetizers):
    """Determine which `dishes` are designated `appetizers` and remove them.

    :param dishes: list - of dish names.
    :param appetizers: list - of appetizer names.
    :return: list - of dish names that do not appear on appetizer list.

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    """
    print(type(dishes))
    print(dishes)
    print(type(appetizers))
    print(appetizers)
    new_list = set(dishes).difference(appetizers)
    return list(new_list)


separate_appetizers(['Avocado Deviled Eggs','Flank Steak with Chimichurri and Asparagus', 'Kingfish Lettuce Cups',
             'Grilled Flank Steak with Caesar Salad','Vegetarian Khoresh Bademjan','Avocado Deviled Eggs',
             'Barley Risotto','Kingfish Lettuce Cups'], ['Kingfish Lettuce Cups','Avocado Deviled Eggs','Satay Steak Skewers',
              'Dahi Puri with Black Chickpeas','Avocado Deviled Eggs','Asparagus Puffs',
              'Asparagus Puffs'])

def singleton_ingredients(dishes, intersection):
    """Determine which `dishes` have a singleton ingredient (an ingredient that only appears once across dishes).

    :param dishes: list - of ingredient sets.
    :param intersection: constant - can be one of `<CATEGORY>_INTERSECTIONS` constants imported from `sets_categories_data.py`.
    :return: set - containing singleton ingredients.

    Each dish is represented by a `set` of its ingredients.

    Each `<CATEGORY>_INTERSECTIONS` is an `intersection` of all dishes in the category. `<CATEGORY>` can be any one of:
        (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).

    The function should return a `set` of ingredients that only appear in a single dish.
    """
    all_ingredients = set().union(*dishes)
    return all_ingredients - intersection