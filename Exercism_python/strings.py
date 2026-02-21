#Learning
single_quoted = 'These allow "double quoting" without "escape" characters.'
double_quoted = "These allow embedded 'single quoting', so you don't have to use an 'escape' character"

triple_quoted = '''Three single quotes or "double quotes" in a row allow for multi-line string literals.
  Line break characters, tabs and other whitespace is fully supported. Remember - The escape "\" character is also available if needed (as can be seen below). 
  
  You\'ll most often encounter multi-line strings as "doc strings" or "doc tests" written just below the first line of a function or class definition.
    They\'re often used with auto documentation ✍ tools.
    '''
my_number = 42
new_num = str(my_number)
print(new_num)
print(type(new_num))
#"42"

numbers = [1,3,5,7]
my_num = str(numbers)
print(my_num)
print(type(my_num))
#'[1,3,5,7]'

creative = '창의적인'
print(creative[0])
print(creative[1])
print(creative[2])
print(len(creative[0]))
print(type(creative))
print(creative[0:1])

moon_and_stars = '🌟🌟🌙🌟🌟⭐'
print(moon_and_stars[:-1])
print(moon_and_stars[:-2])
print(moon_and_stars[:-3])
print(moon_and_stars[:-4])
print(moon_and_stars[2:3])
print(moon_and_stars[2:])
print(moon_and_stars[2:4])
print(moon_and_stars[4:5])

cat_ipsum = "Destroy house in 5 seconds command the hooman."
cat_split = cat_ipsum.split()
print(cat_split)
#['Destroy', 'house', 'in', '5', 'seconds', 'command', 'the', 'hooman.']

cat_words = "feline, four-footed, ferocious, furry"
new_split = cat_words.split(',')
print(new_split)
#['feline', ' four-footed', ' ferocious', ' furry']

chickens = ["hen", "egg", "rooster"] # Lists are iterable.
new_list = (' '.join(chickens))
print(new_list)
#'hen egg rooster'
#' 🌿 '.join(chickens)
#'hen 🌿 egg 🌿 rooster'

flowers = ("rose", "daisy", "carnation")  # Tuples are iterable.
flower_list = '*-*'.join(flowers)
print(flower_list)
#'rose*-*daisy*-*carnation'

phrase = "This is my string"  # Strings are iterable, but be careful!
new_phrase = '..'.join(phrase)
print(new_phrase)
#'T..h..i..s.. ..i..s.. ..m..y.. ..s..t..r..i..n..g'
# Separators are inserted **between** elements, but can be any string (including spaces).

under_words = ['under', 'current', 'sea', 'pin', 'dog', 'lay']
separator = ' ⤴️ under' # Note the leading space, but no trailing space.
new_separator = separator.join(under_words)
print(new_separator)
#'under ⤴️ undercurrent ⤴️ undersea ⤴️ underpin ⤴️ underdog ⤴️ underlay'

# Exercises
def remove_suffix_ness(word):
    my_new_list_one = []
    #print(word[0][:-5])
    for new_word in word:
        new_word = new_word[:-4]
        if(new_word[-1] == "i"): 
            #print(new_word[-1])
            new_word= new_word[:-1] + "y"
            #print (new_word)
        my_new_list_one.append(new_word)
    print(my_new_list_one)
    return my_new_list_one

#remove_suffix_ness(['heaviness', 'sadness', 'softness', 'crabbiness', 'lightness', 'artiness', 'edginess'])

#Exercise 4

def adjective_to_verb(sentence, index):
    print(sentence[4])
    new_sentence = sentence.replace(".", "")
    print(new_sentence)
    word = new_sentence.split()[index] + "en"
    print(word)
    return word

adjective_to_verb("His expression went dark.", -1)

single_quoted = 'Hello this is a "string" and I wrote the string'
double_quoted = "This is a double string 'I am writing' Hello"
escapes = 'This is a string \' Hello \' I\'m saying \' Hi \' '

'''
Multi-line string
This is a string that has multiple lines
Hello 
Bye
'''

"""
This is another multi-line string 
with three double quoted 
Hello
Bye
"""

name = "Laura"
age = "29"
language = "spanish"

phrase = name + " has " + age + " years. " + "She speaks " + language
#print(phrase)

animals = ["Dog", "Cat", "Penguin", "Whale", "Squirtle", "Hamster"]
animals_join = ' 🐹 '.join(animals)
#print (animals_join)

chickens = ["hen", "egg", "rooster"]
cosa = ' : '.join(chickens)
##print (cosa)

word_1 = "Supercalifragilestilistiqualidoso"
#print(word_1[1])
#print(word_1[-1])
#print(word_1[-11])
#print(word_1[11])

moon_and_stars = '🌟🌟🌙🌟🌟⭐'
sun_and_moon = '🌞🌙🌞🌙🌞🌙🌞🌙🌞'

#print(moon_and_stars[1:4])

phrase2 = "This is an amazing phrase about some topic"
#print(phrase2.split())
phrase2.split()
#print(phrase2.split()[2])

#exercise #1 add a prefix to a word
def add_prefix_un(word):
    return 'un' + word 

"""def make_word_groups(vocab_words):
    my_new_list = []
    prefix = vocab_words[0]
    print (prefix)
    for word_exercise in range(1, len(vocab_words)):
        whole_word = prefix + word_exercise
        print (whole_word)
        my_new_list.append(whole_word)
    print(my_new_list)
    final_list = ' :: '.join(my_new_list)
    print(final_list)
    return vocab_words

make_word_groups(['en', 'close', 'joy', 'lighten', 'a', '2', 'e', 'dd', 'ee', 'fef','hoa'])"""
# exercise #2: Add Prefixes to word groups 
def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    new_list = vocab_words[1:len(vocab_words)]
    my_new_list = []
    #print (new_list)

    for word_in_list in new_list:
        whole_world = prefix + word_in_list
        #print(whole_world)
        my_new_list.append(whole_world)
    my_new_list.insert(0, prefix)
    print(my_new_list)
    final_list = ' :: '.join(my_new_list)
    print(final_list)
    return final_list

#make_word_groups(['en', 'close', 'joy', 'lighten', 'a', '2', 'e', 'dd'])

# Exercise 3 remove sufix

def remove_suffix_ness(word_lala):
    my_new_list_one = []
    print(word_lala[0][:-5])
    for new_word in word_lala:
        new_word = new_word[:-4]
        if(new_word[-1] == "i"): 
            print(new_word[-1])
            new_word= new_word[:-1] + "y"
            print (new_word)
        my_new_list_one.append(new_word)
    print(my_new_list_one)
    return new_word

remove_suffix_ness(['heaviness', 'sadness', 'softness', 'crabbiness', 'lightness', 'artiness', 'edginess'])

mi_lista = ["Hola", "Mundo", "Python"]

# Modificar la segunda letra del primer elemento ("Hola")
mi_lista[0] = mi_lista[0][:1] + "i" 
print (mi_lista)