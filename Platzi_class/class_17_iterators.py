my_list = [1,2,3,4]

my_iter = iter(my_list)

#use the iterator
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

#chains iteration
text = "Hola Mundo"
iter_text = iter(text)
for char in iter_text:
    print(char)

# iterator for odd numbers
limit = 10
odd_itter = iter(range(1, limit+1, 2))  # range(start, stop, step)
for num in odd_itter:
    print(num)

#generator
def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)

#fibonacci
# 0 1 1 2 3 5 8 13 21...
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b
for num in fibonacci(10):
    print(num)

