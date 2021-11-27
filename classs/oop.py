# OOP Exercise 5: Define a property that must have the same value for every class instance (object)

# Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
# Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18

class Vehicle:

    color= "white"

    def __init__(self,name,max_speed,year):
        self.name = name;
        self.max_speed = max_speed
        self.year = year

    def assigning_value(self):
        print("name",self.name)
        print("maax-speed",self.max_speed)
        print("year",self.year)

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

bus = Bus("mercedes",231,123);
bus.assigning_value()

car = Car("audi",123,12)
car.assigning_value()
        
