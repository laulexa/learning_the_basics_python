class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"the vehicle {self.brand}. Has been sold")
        else:
            print(f"the vehicle {self.brand}. Is not available")
    
    def check_available(self):
        return self.is_available

    def get_price(self):
        return self.price
    
    def start_engine(self):
        raise NotImplementedError("This method needs to be implemented for the subclass")
    
    def stop_engine(self):
        raise NotImplementedError("This method needs to be implemented for the subclass")
    
class Car(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"The car engine {self.brand} is running"
        else:
            return f"The car {self.brand} is not available"
        
    def stop_engine(self):
        if self.is_available:
            return f"The car engine {self.brand} has stopped"
        else:
            return f"The car {self.brand} is not available"
        
class Bike(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"The bicycle {self.brand} is running"
        else:
            return f"The bicycle {self.brand} is not available"
        
    def stop_engine(self):
        if self.is_available:
            return f"The bicycle {self.brand} has stopped"
        else:
            return f"The bicycle {self.brand} is not available"
        
class Truck(Vehicle): 
    def start_engine(self):
        if not self.is_available:
            return f"The Truck engine{self.brand} is running"
        else:
            return f"The Truck{self.brand} is not available"
        
    def stop_engine(self):
        if self.is_available:
            return f"The Truck engine {self.brand} has stopped"
        else:
            return f"The Truck {self.brand} is not available"
        
class Customer:
    def __init__(self,name):
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self, vehicle:Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"I'm sorry, {vehicle.brand} is not available")
    
    def inquire_vehicle(self, vehicle:Vehicle):
        if vehicle.check_available():
            availability = "Available"
        else:
            availability = "Not available"
        print(f"The {vehicle.brand} is {availability} and it costs {vehicle.get_price()}")

class Dealership: 
    def __init__(self):
        self.inventory = []
        self.customers = []
    
    def add_vehicles(self, vehicle):
        self.inventory.append(vehicle)
        print(f"The {vehicle.brand} has been added to the inventory")
    
    def register_customers(self, customer:Customer):
        self.customers.append(customer)
        print(f"The customer {customer.name} has been added")
    
    def show_available_vehicle(self):
        print("Vehicles available in the store")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"- {vehicle.brand} for { vehicle.get_price()}")

car1 = Car("Toyota", "Corolla", 20000)
bike1 = Bike("Yamaha", "MT-07", 7000)
truck1 = Truck("Volvo", "FH16", 80000)

customer1 = Customer("Carlos")

dealership = Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)

#show available vehicles
dealership.show_available_vehicle()

#Customer ask for a vehicle
customer1.inquire_vehicle(car1)

#Customer buys car
customer1.buy_vehicle(car1)

#available vehicles
dealership.show_available_vehicle()
    

