print("Hola Mundo")

'''name = input("Please tell us your name: ")
print(name)
print(type(name))
age = input("please tell us your age: ")
print(type(age))'''
#input returns an string even if I write a number, this will be class 'str' I should add an int to be able to treat this number as an integer like this
#age = int(input("please tell us your age: "))

to_do = ["head out to the hotel", "have lunch", "visit a museum", "go back to the hotel"]
print(to_do)

numbers = [1, 2, 3, 4, "five"]
print(type(numbers))

mix = [1, "Two", 3.14, True, [1, 2, 3]]
print(mix)
print(len(mix))
print("first element:", mix[0])
print("second element:", mix[1])
print("last element:", mix[-1])

string = "Hola Mundo"
print("first element:", string[0])
print("second element:", string[1])
print("last element:", string[-1])
print(mix[0:3]) #it doesn't include the value of 3 , just 0 , 1 and 2  [1, 'Two', 3.14]
print(mix[2:]) #[3.14, True, [1, 2, 3]]
print(mix[2:-2]) #[3.14]

mix.append(False) 
print(mix) #[1, 'Two', 3.14, True, [1, 2, 3], False]
mix.append(["a", "b"])
print(mix) # [1, 'Two', 3.14, True, [1, 2, 3], False, ['a', 'b']]

mix.insert(1, ["a", "b"]) # 
print(mix) # [1, ['a', 'b'], 'Two', 3.14, True, [1, 2, 3], False, ['a', 'b']]

print(mix.index(["a", "b"])) # 1 index returns the first coincidence

more_numbers = [1, 32, 42, 232, 1, 12, 33, 232, 1,53, 443, 2]
print("Max:", max(more_numbers)) #Max: 443
print("Min:", min(more_numbers)) #Min: 1

del more_numbers[-1]
print(more_numbers) #[1, 32, 42, 232, 1, 12, 33, 232, 1, 53, 443]

del more_numbers[0:2]
print(more_numbers) #[42, 232, 1, 12, 33, 232, 1, 53, 443]

#del more_numbers