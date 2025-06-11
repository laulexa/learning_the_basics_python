a = [1,2,3,4,5]
b = a

print(a) # [1, 2, 3, 4, 5]
print(b) # [1, 2, 3, 4, 5]

del a [0]
print(a) #[2, 3, 4, 5]
print(b) #[2, 3, 4, 5]
print(id(a)) # 2450050277568 same id
print(id(b)) # 2450050277568 same id

c = a[:]
print(id(a))
print(id(b))
print(id(c)) # 2265558434624 different id
a.append(6)
print(a) #[2, 3, 4, 5, 6]
print(b) #[2, 3, 4, 5, 6]
print(c) #[2, 3, 4, 5]