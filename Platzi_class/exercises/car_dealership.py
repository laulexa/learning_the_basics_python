class Vehicle:
    def __init__(self, brand, units, price):
        self.brand = brand
        self.price = price
        self.available = True
        self.units = units

    def car_availability(self):
        self.available = True
        print(f"the car {self.brand} is available")
        
    def car_purchase(self, units):
        if units >= 1:
            print(f"there are {self.units} cars available")
        else:
            self.available = False
            print("There are no cars available")

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_ide = user_id
        self.cars_bought = []
    
    def buy_car(self, vehicle):
        if vehicle.available:
            vehicle.car_purchase()
            self.available_cars.append(vehicle)
        else:
            (f"The car {vehicle.brand} Is not available")

    def return_book(self,book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"The book {book.title} isn't in the list of borrowed books")


vehicle1 = Vehicle("Ford",2, 5000)
vehicle1.car_availability()
vehicle1.car_purchase(2)
    

#Available, price, buy one