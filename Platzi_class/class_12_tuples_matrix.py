matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matrix) #[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0]) #[1, 2, 3]
print(type(matrix)) #<class 'list'>

#tuple
numbers = (1,2,3,4,5)
print(numbers)
print(type(numbers)) #<class 'tuple'>
print(numbers[0])
#numbers[0] = 'unos' error Tuples are immutable

#for tuples I use () and for lists I use []

#We can add a list inside a tuple
numbers2 = (7,8,9,10,[11,12])
print(numbers2) #(7, 8, 9, 10, [11, 12])
print(numbers2[4]) #[11, 12]
print(type(numbers2[4]))  #<class 'list'>
numbers2[4][1] = 2
print(numbers2) #(7, 8, 9, 10, [11, 2]) we could modify the list inside the tuple