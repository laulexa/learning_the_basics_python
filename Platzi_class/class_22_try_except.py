try:
    divisor = int(input("enter a divisor number:"))
    result = 100 / divisor
    print(result)
except ZeroDivisionError as e:
    print("Error: the divisor can't be 0")
    print("There has been an error:", e)
except ValueError as e:
    print("Error: You should enter a valid number")
    print("There has been an error:", e)