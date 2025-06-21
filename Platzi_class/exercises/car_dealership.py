class Vehicle:
    def __init__(self, brand, model, units, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.available = True
#        self.units = units

    def car_sold(self):
        if self.available:
            self.available = False
            print(f"the car {self.brand} {self.model} has been sold")
        else:
            print(f"the car {self.brand} {self.model} is not available")

    def check_availability(self):
        return self.available
    
    def get_price(self):
        return self.price

''' def car_purchase(self, units):
        if units >= 1:
            print(f"there are {self.units} cars available")
        else:
            self.available = False
            print("There are no cars available")'''

class Customer:
    def __init__(self, name, user_id):
        self.name = name
        self.user_ide = user_id
        self.cars_bought = []
    
    def buy_car(self, vehicle):
        if vehicle.check_availability():
            vehicle.car_sold()
            self.cars_bought.append(vehicle)
        else:
            (f"The car {vehicle.brand} {vehicle.model} Is not available")

    def inquire_vehicle(self, vehicle):
        availability = "available" if vehicle.check_availability() else "not available"
        print(f"The vehicle {vehicle.brand} {vehicle.model} is {availability} and the price is: {vehicle.price}")

class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []
    
    def add_car(self, vehicle):
        self.inventory.append(vehicle)
        print(f"the car {vehicle.brand} {vehicle.model} has been added to the inventory")
    
    def register_customer(self, customer):
        self.customers.append(customer)
        print(f"The customer {customer.name} has been added to the car dealership")

    def show_available_cars(self):
        print("The available cars in the car dealership are: ")
        for vehicle in self.inventory:
            if vehicle.check_availability():
                print(f"- {vehicle.brand} {vehicle.model} is {vehicle.get_price()}")




vehicle1 = Vehicle("Ford",2, 5000)
vehicle1.car_availability()
vehicle1.car_purchase(2)
    

#Available, price, buy one