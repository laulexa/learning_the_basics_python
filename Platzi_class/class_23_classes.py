class Person:
    def __init__(self, name, age):
        self.name  = name
        self.age = age

    def greet(self):
        print(f"Hi my name is {self.name} and I am {self.age}")

person1 = Person("Anna", 30)    
person2 = Person("Luis", 25)

person1.greet()
person2.greet()