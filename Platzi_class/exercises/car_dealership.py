class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True
#        self.units = units

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"the car {self.brand} {self.model} has been sold")
        else:
            print("Hola")
            print(f"the car {self.brand} {self.model} is not available")

    def check_availability(self):
        return self.is_available
    
    def get_price(self):
        return self.price

class Customer:
    def __init__(self, name):
        self.name = name
        self.cars_purchased = []
    
    def buy_car(self, car):
        if car.check_availability():
            car.sell()
            self.cars_purchased.append(car)
        else:
            print(f"The car {car.brand} {car.model} Is not available")

    def inquire_car(self, car):
        availability = "available" if car.check_availability() else "not available"
        print(f"The car {car.brand} {car.model} is {availability} and the price is: {car.price}")

class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []
    
    def add_car(self, car):
        self.inventory.append(car)
        print(f"the car {car.brand} {car.model} has been added to the inventory")
    
    def register_customer(self, customer):
        self.customers.append(customer)
        print(f"The customer {customer.name} has been added to the car dealership")

    def show_available_cars(self):
        print("The available cars in the car dealership are: ")
        for car in self.inventory:
            if car.check_availability():
                print(f"- {car.brand} {car.model} is {car.get_price()}")



#Create cars
car1 = Car("Ford","500", 5000)
car2 = Car("Mazda","CX-50", 35000)
car3 = Car("TOYOTA","Corolla", 25000)

#Create clients
customer1 = Customer("Carlos")

#create the dealership and add cars and clients
dealership = Dealership()
dealership.add_car(car1)
dealership.add_car(car2)
dealership.add_car(car3)
dealership.register_customer(customer1)

#Show available cars
dealership.show_available_cars()

#Client inquire a car
customer1.inquire_car(car1)

# Client buys a car
customer1.buy_car(car1)

#Show available cars again
dealership.show_available_cars()

customer1.inquire_car(car2)
customer1.inquire_car(car3)

customer1.buy_car(car2)
dealership.show_available_cars()

customer1.buy_car(car3)
dealership.show_available_cars()

customer1.buy_car(car1)
customer1.buy_car(car2)
customer1.buy_car(car3)

customer1.inquire_car(car1)
customer1.inquire_car(car2)
customer1.inquire_car(car3)


#Client tries to buy a sold car

