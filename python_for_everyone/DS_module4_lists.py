#8.4 Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split() method.
# The program should build a list of words.
# For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in python sort() order as shown in the desired output

'''fname = input("Enter file name: ")
fh = open(fname)
lst = list()
new_list = []
for line in fh:
    #print(line.rstrip())
    new_line =line.split()
    #print(new_line)
    #print(type(new_line))
    lst.append(new_line)
for sublist in lst:
    #new_list.extend(sublist)
    for item in sublist:
        if item in new_list:
            continue
        new_list .append(item)
print(new_list)
new_list.sort()
print(new_list)
print("Sorted:", new_list)
'''
# remember strings are immutable, to add them to a list you have to create a new variable

#improved version
fname = input("Enter file name: ")
fh = open(fname)
new_list = []

for line in fh:
    # Split the line into words immediately
    words = line.split()
    print("words:", words)
    # Loop through the words in this specific line
    for word in words:
        # Check if we already have the word to keep it unique
        if word not in new_list:
            new_list.append(word)

new_list.sort()
print("Sorted:", new_list)