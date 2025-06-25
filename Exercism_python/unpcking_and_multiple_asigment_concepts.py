a, b = 2, 3
print(a)
print(b)

c, d, e, f, g = True, "Hello", 2, 3.14, False
print(c)
print(d)
print(e)
print(f)
print(g)

# Multiple assignment can be used to swap elements in lists. This practice is pretty common in sorting algorithms. 
numbers = [1,2]
numbers[0], numbers[1] = numbers[1], numbers[0]
print(numbers) # [2,1]

#Since tuples are immutable, you can't swap elements in a tuple.