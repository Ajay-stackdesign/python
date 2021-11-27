#creating a class with constructorr:

# from _typeshed import Self


# class Parent:

#     def __init__ (self,name,age,salary):
#         self.name = name ;
#         self.age = age;
#         self.salary = salary ;

#     def show_details(self):
#         print("the name of the parent is",self.name)
#         print("the age ogf the employes is",self.age);
#         print("the salary of the empployer is",self.salary)

# my = Parent("ajay",23,234);

# my.show_details()


class Parent1:
    
    def one(self,name,age):
        self.name = name ;
        self.age = age ;

    def show_details_one(self):
        return self.name
        # print("the name of the parent 1 is",self.name)
        # print("the age of the parent1",self.age)

class Parent2: 

    def two(self,name,age):
        self.name = name
        self.age = age

    def show_details_two(self):
        return self.name
        # print("the nme of the parent2 is",self.name)
        # print("the age of the parent2 is",self.age)
    
class Child(Parent1,Parent2):

    def three(self,name,age):
        self.name = name;
        self.age = age;

    def show_details_three(self):
        return self.name

my_child = Child()

my_child.one("ajay",23)
print(my_child.show_details_one())

my_child.two("geeta",51)
print(my_child.show_details_two())

my_child.three("nidhi",23)
print(my_child.show_details_three())


    