x = 5
if x > 5:
    print("X is greater than 5")
elif x == 5:
    print("x is equal to 5")
else: 
    print("X is less than 5 ")
print('we are out of the if')

a = 15
b = 20

if a > 10 and b > 25:
    print("a is greater than 10 and b is greater than 25")
if a > 10 or a > 25:
    print("a is greater than 10 or b is greater than 25")

if not a > 10:
    print("a is not greater than 10")

is_member = False  
age = 11

if is_member:
    if age >= 15:
        print("You have access because you are greater or equal than 15")
    else:
        print("You are a member but you don't have access because you have less than 15 years")
else:
    print("You are not a member and you don't have access")




