import re
name = input("Enter file:")
if len(name) < 1:
    name = "sample_data.txt"
handle = open(name)
numList = list()
count = 0
numOfnums = 0

for line in handle:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    if len(x) > 0:
        for num in x:
            numList.append(num)
    #print(x)

for num in numList:
    count = count + int(num)

print(count)
numOfnums = len(numList)
#print('nums total: ', numOfnums)
#print(numList)

'''x = ' We just have $10 for 3 cookies 5 breads and 32 pans'
y = re.findall('[0-9.]+', x)
print(y)'''