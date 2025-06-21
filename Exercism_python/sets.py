one_element = {'😀'}
multiple_elements = {'😀','😁','😂','😄'}
multiple_elements2 = {'😀','😁','😂','😄', '😂','😄','😂','😄','😄'}
multiple_elements2 = {'😀','😁','😂','😄', '😂','😄','😂','😄','😄'}
print(type(multiple_elements2))
print(multiple_elements2)

names = {"patricia", "laura", "pedro", "Carolina", "Paul", "pedro", "pedro"}

lowercase_set = {item.lower() for item in names}

print(lowercase_set)
print(names)

#create an empty set
no_elements = set()
# elements from a tuple (duplicates are removed)
elements_from_a_tuple = set(("parrot", "whale", "dog", "cat", "dog", "cat"))
print(elements_from_a_tuple)
#elements from a list, (duplicates are removed)
elements_from_a_list = set([1,2,2,3,4,5,5,5,5,6,7,8,9,9,7,2,8,8])
print(elements_from_a_list)
#elements with a string
elements_string = set("Laura")
elements_string_2 = set("timbuktu")
print(elements_string)
print(elements_string_2)

# Attempting to use a list for a set member throws a TypeError : TypeError: unhashable type: 'list'
'''lists_as_elements = {['😅','🤣'], 
                    ['😂','🙂','🙃'], 
                    ['😜', '🤪', '😝']}'''

# Standard sets are mutable, so they cannot be hashed. TypeError: unhashable type: 'set'
'''sets_as_elements = {{'😅','🤣'}, 
                    {'😂','🙂','🙃'}, 
                    {'😜', '🤪', '😝'}}'''
# Both mammals and additional_animals are lists.
mammals = ['squirrel','dog','cat','cow', 'tiger', 'elephant']
additional_animals = ['pangolin', 'panda', 'parrot','lemur', 'tiger', 'pangolin']

# Animals is a dict.
animals = {'chicken': 'white',
               'sparrow': 'grey',
               'eagle': 'brown and white',
               'albatross': 'grey and white',
               'crow': 'black',
               'elephant': 'grey', 
               'dog': 'rust',
               'cow': 'black and white',
               'tiger': 'orange and black',
               'cat': 'grey',
               'squirrel': 'black'}

# Birds is a set.
birds = {'crow','sparrow','eagle','chicken', 'albatross'}

# Mammals and birds don't share any elements.
birds.isdisjoint(mammals)
#True

# There are also no shared elements between 
# additional_animals and birds
birds.isdisjoint(additional_animals)
#True

# Animals and mammals have shared elements.
# **Note** The first object needs to be a set or converted to a set
# since .isdisjoint() is a set method.
set(animals).isdisjoint(mammals)
#False

#Subsets and Supersets
# <set>.issubset(<other_collection>) is used to check if every element in <set> is also in <other_collection>. 
# The operator form is <set> <= <other_set>:

# Set methods will take any iterable as an argument.
# All members of birds are also members of animals.
birds.issubset(animals)
#True

# All members of mammals also appear in animals.
# **Note** The first object needs to be a set or converted to a set
# since .issubset() is a set method.
set(mammals).issubset(animals)
#True

# Both objects need to be sets to use a set operator
birds <= set(mammals)
#False

# A set is always a loose subset of itself.
set(additional_animals) <= set(additional_animals)
#True