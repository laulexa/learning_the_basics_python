add = lambda a, b: a  + b
print(add(10,4))

multiplication = lambda a, b: a * b
print(multiplication(12, 2))

numbers = range(11)
squared_numbers = list(map(lambda x: x**2, numbers))
print("cuadrados:", squared_numbers)

#even
even_numbers = list(filter(lambda x:  x % 2 == 0, numbers))
print("even numbers:", even_numbers)