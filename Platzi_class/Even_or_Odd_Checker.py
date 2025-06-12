#Goal: Ask the user to enter a number and tell them if it's even or odd.
#If the user enters something that's not a valid number, print an error message.

user_number = input("please enter a number: ")

if user_number.isdigit():
    number = int(user_number)
    if number % 2 == 0:
        print("That's an even number!")
    else: 
        print ("That's an odd number!")
else:
    print("That\'s not a valid number. Try again.")