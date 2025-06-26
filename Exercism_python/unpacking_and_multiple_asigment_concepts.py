#Multiple assignment
a, b = 2, 3
print(a)
print(b)

c, d, e, f, g = True, "Hello", 2, 3.14, False
print(c)
print(d)
print(e)
print(f)
print(g)

# Multiple assignment can be used to swap elements in lists. This practice is pretty common in sorting algorithms. 
numbers = [1,2]
numbers[0], numbers[1] = numbers[1], numbers[0]
print(numbers) # [2,1]

#Since tuples are immutable, you can't swap elements in a tuple.
#___________________________________________________________________________________________________________________________________________
#UNPACKING
#In Python, it is possible to unpack the elements of list/tuple/dictionary into distinct variables. Since values appear within lists/tuples in a specific order, they are unpacked into variables in the same order
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#If there are values that are not needed then you can use _ to flag them:
vegetables = ["broccoli", "Spinach", "Celery"]
_,_,m = vegetables
print(m) #Celery

#Deep unpacking
#Unpacking and assigning values from a list/tuple enclosed inside a list or tuple (also known as nested lists/tuples) works in the same way a shallow unpacking does
fruits_vegetables = [["apple", "banana"],["carrot",'potato']]
[[h,i],[j,k]] = fruits_vegetables
print(h)
print(i)
print(j)
print(k)
#You can also deeply unpack just a portion of a nested list/tuple:
fruits_vegetables_2 = [["apple", "banana"],["carrot",'potato']]
[n,[o, p]] = fruits_vegetables_2
print(n) #['apple', 'banana']
print(o) #carrot
print(p) #potato

#Unpacking a list/tuple with *
#When unpacking a list/tuple you can use the * operator to capture the "leftover" values. This is clearer than slicing the list/tuple

colors = ["pink", "Yellow", "gray", "brown", "white", "red"]
s, *last = colors
print(s) #pink
print(last)#['Yellow', 'gray', 'brown', 'white', 'red']

#We can also extract the values at the beginning and end of the list while grouping all the values in the middle:
colors_2 = ["pink", "Yellow", "gray", "brown", "white", "red", "orange", "green"]
t, *middle, u, v= colors_2
print(t) #pink
print(middle) #['Yellow', 'gray', 'brown', 'white', 'red']
print(u) # orange
print(v) #green

#We can also use * in deep unpacking:
fruits_vegetables_3 = [["apple", "banana", "melon"], ["carrot", "potato", "tomato"]]
[[w,*rest],q] = fruits_vegetables_3
print(w) #apple
print(rest) #['banana', 'melon']
print(q) #['carrot', 'potato', 'tomato']

#Unpacking a dictionary
#Iteration over dictionaries defaults to the keys. So when unpacking a dict, you can only unpack the keys and not the values:

fruits_inventory = {"apple": 6, "banana": 2, "cherry": 3}
x,y,z  = fruits_inventory
print(x) #apple
print(y) #banana
print(z) #cherry

#If you want to unpack the values then you can use the <dict>.values() method
x,y,z = fruits_inventory.values()
print(x) #6
print(y) #2
print(z) #3

#If both keys and values are needed, use the <dict>.items() method. <dict>.items() generates an iterable view containing key-value pairs. 
#These can be unpacked into a tuple:

x,y,z = fruits_inventory.items()
print(x) #('apple', 6)
print(y) #('banana', 2)
print(z) #('cherry', 3)
#___________________________________________________________________________________________________________________________________________
#PACKING
#Packing is the ability to group multiple values into one list that is assigned to a variable. This is useful when you want to unpack values, 
# make changes, and then pack the results back into a variable. It also makes it possible to perform merges on 2 or more lists/tuples/dicts.

#Packing a list/tuple with *
#Packing a list/tuple can be done using the * operator. This will pack all the values into a list/tuple.

fruits = ("apple", "banana", "cherry")
more_fruits = ["orange", "kiwi", "melon", "mango"]

## If there is no * on to the left of the "=" the result is a tuple
combined_fruits = *fruits, *more_fruits
print(combined_fruits) #('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')

# If the * operator is used on the left side of "=" the result is a list.
# Note the trailing comma.

*combined_fruits_too, = *fruits, *more_fruits
print(combined_fruits_too) # ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']

#Packing a dictionary with **
#Packing a dictionary is done by using the ** operator. This will pack all key-value pairs from one dictionary into another dictionary, or combine two dictionaries together

fruits_inventory = {"apple": 6, "banana": 2, "cherry": 3}
more_fruits_inventory = {"orange": 4, "kiwi": 1, "melon": 2, "mango": 3}
combined_fruits_inventory = {**fruits_inventory, **more_fruits_inventory}

# then the pairs are packed into combined_fruits_inventory
print(combined_fruits_inventory) #{'apple': 6, 'banana': 2, 'cherry': 3, 'orange': 4, 'kiwi': 1, 'melon': 2, 'mango': 3}

#Usage of * and ** with functions
#Packing with function parameters

#When you create a function that accepts an arbitrary number of arguments, you can use *args or **kwargs in the function definition. 
# *args is used to pack an arbitrary number of positional (non-keyword) arguments as a tuple and 
# **kwargs is used to pack an arbitrary number of keyword arguments as a dictionary.

#Usage of *args:
def my_function(*args):
    print(args)
## Arguments given to the function are packed into a tuple
my_function(1, 2, 3) #(1, 2, 3)
my_function("Hello") #(1, 2, 3, 'Hello', 'Mars')
my_function(1, 2, 3, "Hello", "Mars") #(1, 2, 3, 'Hello', 'Mars')

#Usage of **kwargs:
def my_function(**kwargs):
    print(kwargs)
my_function(a=1, b=2, c=3) # {"a": 1, "b": 2, "c": 3}

#*args and **kwargs can also be used in combination with one another:

def my_function(*args, **kwargs):
    print(sum(args))
    for key, value in kwargs.items():
        print(str(key)+ " = " + str(value))

my_function(1,2,3, a=1,b=2,c=3)

#6
#a = 1
#b = 2
#c = 3
#You can also write parameters before *args to allow for specific positional arguments. Individual keyword arguments then have to appear before **kwargs.

'''Arguments have to be structured like this:
def my_function(<positional_args>, *args, <key-word_args>, **kwargs)
If you don't follow this order then you will get an error.'''

def my_function(a, b, *args):
    print(a)
    print(b)
    print(args)

my_function(1, 2, 3, 4, 5)
#1
#2
#(3, 4, 5)

#Writing arguments in an incorrect order will result in an error:
# def my_function(*args, a, b):
   # print(args)

#Unpacking into function calls
#You can use * to unpack a list/tuple of arguments into a function call. This is very useful for functions that don't accept an iterable:

def my_function(a, b, c):
    print(c)
    print(b)
    print(a)

numbers = [1,2,3]
my_function(*numbers)

#3
#2
#1

#Using * unpacking with the zip() function is another common use case. 
# Since zip() takes multiple iterables and returns a list of tuples with the values from each iterable grouped:

values = (['x', 'y', 'z'], [1, 2, 3], [True, False, True])
a, *rest = zip(*values)
print(rest) #[('y', 2, False), ('z', 3, True)]
print(a) # ('x', 1, True)