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
