numbers = {1:"One", 2:"Two", 3:"Three"}
print(numbers[2]) #Two
information = {"name": "carla",
               "Last name": "Mendez",
               "Heigh": 1.60,
               "age": 32}
del information["age"]
print(information) #{'name': 'carla', 'Last name': 'Mendez', 'Heigh': 1.6}

claves = information.keys()
print(claves) #dict_keys(['name', 'Last name', 'Heigh'])
print(type(claves)) #<class 'dict_keys'>
values = information.values()
print(values) #dict_values(['carla', 'Mendez', 1.6])
pairs = information.items()
print(pairs) #dict_items([('name', 'carla'), ('Last name', 'Mendez'), ('Heigh', 1.6)])

contacts = {"Lilia":{"Last name": "Cardona",
               "Heigh": 1.50,
               "age": 35},
               "Diego": {"Last name": "Ramirez",
               "Heigh": 1.80,
               "age": 22}}

print(contacts) #{'Lilia': {'Last name': 'Cardona', 'Heigh': 1.5, 'age': 35}, 'Diego': {'Last name': 'Ramirez', 'Heigh': 1.8, 'age': 22}}
print(contacts["Lilia"]) #{'Last name': 'Cardona', 'Heigh': 1.5, 'age': 35}

# Contador de palabras
palabras = ["manzana", "banana", "naranja", "manzana", "banana"]
contador = {}
for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1
print("Contador de palabras:", contador) #{'manzana': 2, 'banana': 2, 'naranja': 1}
