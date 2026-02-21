#10.2 Write a program to read through the mbox-short.txt 
# and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
my_list = list()
my_dict = dict()

for line in handle:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    new_word = words[5].split(':')
   #print(new_word[0])
    my_list.append(new_word[0])
    #print(words[5])

for number in my_list:
    my_dict[number] = my_dict.get(number, 0) + 1

t = sorted(my_dict.items())
#print(t)
for k, v in t:
    print(k, v)
#print(my_list)
#print(my_dict)




'''for number, count in my_dict.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bignumber = number
    print(bignumber , bigcount )
'''
'''for key, value in my_dict:
    print(value, key)'''