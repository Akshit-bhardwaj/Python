# Oops


# class Car:
#     brand = "Toyota"

#     def fuel_type():
#         print("Petrol Car")

# my_car = Car()
# print(my_car.brand)
# my_car.fuel_type()


# class Factory:
#     def __init__(self , price , brand , material = "Good polyster material" ): # Now my material params work as a Default parameter.
#         self.material = material
#         self.price = price
#         self.brand = brand

# obj = Factory(1200 , "Puma")
# print(obj.material)



# class Bagfactory:
#     def __init__(self , material , zips , pocket = 2):
#         self.material = material
#         self.zips = zips
#         self.pocket = pocket

# puma = Bagfactory("Leather" , 3 , 2)

# reebok = Bagfactory("Polyster" , 6 )

# print(reebok.pocket)




# Attributes and functions.


# class Animal:
#     name = "Lion"   

#     @classmethod
#     def class_method(cls):
#         print("Hello I m a class method")

#     def __init__(self , name , age):
#         self.name = name # These are my instance methods.
#         self.age = age
    


#     def show(self): # Instance method
#         print(f"Here's your class details {self.name} , {self.age}")

# obj = Animal("Dog" , 2)
# print(obj.name)

# obj.show()

# obj.class_method()

# Whole example of attributes , class method , instance method , static method , instance variable.



# class School:
#     school_name = "DPS"

#     @classmethod
#     def class_function(cls):
#         print(f" School name is : {cls.school_name}")

#     def __init__(self , year , students , teachers):
#         self.year = year
#         self.students = students
#         self.teachers = teachers

#     @staticmethod
#     def about_school():
#         print("This school is 82 years old , It is very popular due to its highly qulaified teachers.")


# my_school = School(year = 82 , students=4500 , teachers = 122)
# my_school.about_school()

# my_school.class_function()

# print(my_school.school_name)

# print(my_school.year)
# print(my_school.students)
# print(my_school.teachers)



# Inheritance


# class Factorypune:
#     factory_name = "M24"
#     def __init__(self , workers , salary):
#         self.workers = workers
#         self.salary = salary
#     def hello(self):
#         print(f"How many workers are in the company : {self.workers}")

# class Factorymumbai(Factorypune):
#     def __init__(self, workers, salary , age):
#         super().__init__(workers, salary)
#         self.age = age

#     def aboutchild(self):
#         print(f"Age : {self.age}")

# obj1 = Factorypune(45 , 10000)
# obj2 = Factorymumbai(45 , 10000 , 30)
# obj2.aboutchild()
# obj2.hello()


# Multiple Inheritance

# class Animal:
#     def __init__(self , name):
#         self.name = self.name

#     def about_animal(self):
#         print(f"Animal is {self.name}")
    

# class Human:
#     def __init__(self , name , age):
#         self.name , self.age = name , age

# class Robot(Human , Animal):
#     def __init__(self, name, age):
#         super().__init__(name, age)

# obj = Robot("Milli" , 21)
# print(obj.name)
# print(obj.age)




# Multi level Inheritance


# class Grandparents:
#     @classmethod
#     def heritage(cls):
#         print("Heloo I'm in a grandparent class")

# class Parents(Grandparents):
#     @classmethod
#     def parent_heritage(cls):
#         print("Hello I'm in a parents class")

# class Child(Parents):
#     pass


# obj = Child()
# obj.parent_heritage()
# obj.heritage()



# Mini project


# class Factory:
#     def __init__(self , material , zips):
#         self.material = material
#         self.zips = zips

# class Ghaziabadfactory(Factory):
#     def __init__(self, material, zips , color):
#         super().__init__(material, zips)
#         self.color = color

# class Punefactory(Ghaziabadfactory):
#     def __init__(self, material, zips, color , pockets):
#         super().__init__(material, zips, color)
#         self.pockets = pockets

# obj1 = Punefactory("Leather" , 3 , "Black" , 4)
# print(obj1.zips)
# print(obj1.material)
    


class Animal:
    name1 = "Lion"

    def about_animal(self):
        self.breed = "White Lion"
        print(f"I am {self.name1} and my breed is {self.breed}")

class Human(Animal):
    name2 = "Milli"

    def about_human(self):
        print(f"I'm {self.name2} , {self.name1}")


obj = Human()

print(obj.name1)
print(obj.about_animal())