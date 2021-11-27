
# OOP Exercise 1: Create a Class with instance attributes
# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed;
        self.mileage = mileage;

    def show_details(self):
        print("the max spped is",self.max_speed);
        print("the max speed is",self.mileage);

v1 = Vehicle(180,35)
v1.show_details()

# OOP Exercise 2: Create a Vehicle class without any variables and methods

class Vehicle1:
    pass

class Vehicle2:
    def assign_value(self,speed,model,max_mileage):
        self.speed = speed;
        self.model = model;
        self.max_mileage = max_mileage;
    

    def show_details_vehicle2(self):
        print("the speed of the vehicle is",self.speed)
        print("the model of the vehicle is",self.model)
        print("the max_mileage of vehicle is",self.max_mileage)

class Bus(Vehicle2):

    def assigning_value(self,name,year):
        self.name = name;
        self.year = year;


    def show_details_bus(self):
        print("the  name of the bus is",self.name)
        print("the year of the bus is",self.year)

b1 = Bus();

b1.assign_value(22,"ford",24);
b1.show_details_vehicle2();

b1.assigning_value("hatthii",2019)
b1.show_details_bus()



# class Vehicle:
    
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

# Vehicle Name: School Volvo Speed: 180 Mileage: 12

class vehicle3:

    def __init__(self,name,max_speed,mileage):
        self.name =name;
        self.max_speed = max_speed;
        self.mileage = mileage

    def show_of_details(self):
        print("the name of the vehicle is",self.name);
        print("the max_speed of the vehicle is",self.max_speed)
        print("the mileage of the vehicle is",self.mileage);

class Bus1(vehicle3):
    def __init__(self,name,max_speed,mileage,cost):
        super().__init__(name,max_speed,mileage)
        self.cost = cost

    def show_of_bus(self):
        print("the cost of the bus",self.cost)

b1 = Bus1("ford",22,23,2345);
b1.show_of_details()
b1.show_of_bus()

# OOP Exercise 4: Class Inheritance
# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity()
#  a default value of 50.

# Use the following code for your parent Vehicle class.

# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"

class Vehicle5:
    def __init__(self,name,max_speed,mileage):
        self.name = name;
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_position(self,position=50):
        return f"the seating capacity of a {self.name} is {position} passengers"

class Bus(Vehicle5):
    def seating_position(self, position=50):
        return super().seating_position(position=20)
    

b5 = Bus("mercedes",234,23)
bus=b5.seating_position()
print(bus)


class Vehicle6:
    def __init__(self,name,mileage,year):
        self.name = name
        self.mileage = mileage
        self.year = year

    def value_of_seating(self,position):
        return f"the name of the vehicle is {self.name} and the position of seating is {position}"

class Car1(Vehicle):
    def value_of_seating(self,position=24):
        return super().value_of_seating(position=23)

busCa = Car1("ford",23,2015);
busCar = busCa.value_of_seating()
print(busCar)


