def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1) # 
    
factorial_5 = print(factorial(5))


# 2

def counting_number(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + counting_number(n - 1)

print(counting_number(6))