def add(a, b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

def calculator():
    while True:
        print("choose an option")
        print("1. Addition")
        print("2. subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        option = input("enter your option (1, 2, 3, 4, 5)")

        if option == "5":
            print("Exit")
            break
        
        if option in ["1", "2", "3", "4"]:
            num1 = float(input("Enter the first number"))
            num2 = float(input("Enter the second number"))

            if option == "1":
                print("the result of the addition is:", add(num1, num2))
            elif option == "2":
                print("the result of the subtraction is:", subtract(num1, num2))
            elif option == "3":
                print("the result of the multiplication is:", multiply(num1, num2))
            elif option == "4":
                print("the result of the division is:", divide(num1, num2))
        else:
            print("Not valid option, try again")

calculator()
