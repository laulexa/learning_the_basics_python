numbers = [1,2,3,4,5,6]
for i in numbers:
    if i == 3:
        continue
    print("i equals to: ", i)

for i  in range(3, 10):
    print(i) #10 is not included

fruits = ["apple", "pear", "orange", "tomato"]
for fruit in fruits:
    print(fruit)
    if fruit == "orange":
        print("We found the orange!")

x = 0
#while x < 5:
#    print(x)  infinite loop

while x < 5:
    if x == 3:
        break
    print(x)
    x += 1