# class Animal:
#     def __init__(self,age,color):
#         self.age = age
#         self.color = color
#
#     def __str__(self):
#         return self.age + "," + self.color
#
#     def increase_age(self):
#         return int(self.age) + 10
#
# obj1 = Animal(age='3', color='yellow')
#
# obj2 = Animal(age='2', color='white')
#
#
# print(obj1.increase_age())
#
# print(obj2.increase_age())

# Funksiya ve metod anlayislari


# Funksiyalar - > bugune qeder serbest yazdigimiz funksiyalar
# Metod - > obyekte mexsus olan funksiyaya deyirik



# class Person:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#
#     def say_hello(self):
#         return "Hi, everyone"
#
#     def age_increaser(self):
#         return int(self.age) + 2
#
#     def __str__(self):
#         return self.name + " " + self.surname
#
# obj1 = Person(name='Intigam', surname="Guluzade", age="21")
#
# print(obj1.age_increaser())
# print(obj1.say_hello())
# print(obj1.surname)
# print(obj1)


# Inheritance --> Varis alma
# Inheritance --> Bir class-in atribut ve metodlarindan basqa bir class-in istifade etmesi


# class Vehicle:
#     def __init__(self, model, year):
#         self.model = model
#         self.year = year
#
#     def __str__(self):
#         self.model + " " + str(self.year)
#
#
# # DRY --> Dont repeat yourself
#
# class Bike(Vehicle):
#     def __init__(self, model, year, seat):
#         super().__init__(model, year)
#         self.seat = seat
#
#     def __str__(self):
#         return self.model
#
# obj1 = Bike(model="Nissan", year=2010, seat="Comfortable")
# print(obj1)
# print(obj1.model, obj1.year, obj1.seat)


# class Vehicle:
#     def __init__(self, model, year, speed):
#         self.model = model
#         self.year = year
#         self.speed = speed
#
#     def __str__(self):
#         return self.model + " " + str(self.year)
#
#     def show_speed(self):
#         return self.speed
#
#
# class Bike(Vehicle):
#     def __init__(self, model, year, speed, seat):
#         super().__init__(model, year, speed)
#         self.seat = seat
#
#     def __str__(self):
#         return self.model
#
#
# obj1 = Bike(model="Nissan", year=2007, speed=280, seat="Comfortable")
# print(obj1.show_speed())


# class Animal:
#     def __init__(self, age, color):
#         self.age = age
#         self.color = color
#
#     def __str__(self):
#         self.color + " " + str(self.age)
#
#     def count_of_feet(self):
#         return "Heyvanin ayaq sayi"
#
#
# class Cat(Animal):
#     def __init__(self, age, color, name):
#         super().__init__(age, color)
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#     def count_of_feet(self):
#         return "Bala class"
#
# cat1 = Cat(age=3, color="Yellow", name="Mestan")
# print(cat1.count_of_feet())

"""
Bir metod(eyni adda) muxtelif isler gorurse buna polimorfizm anlayisi deyilir.
"""


# mystr = "salam"

# print(len(mystr))

# mytuple = ("sa", "lam", "nece", "siz")
# print(len(mytuple))


# Inheritance, polimorfizm, metod yazmagi.


# Modullar -- > import acar sozu ile inteqrasiya edilir


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def say_hello(self):
        return "Salaam"


# Modullar 3 cur olur: -> 1. Pythonun uzerinde gelenler
# Numpy, math
# 2. Sonradan yuklenen modullar
# pygame, tkinter
# 3. Ozumuzun yaratdigimiz modullar
# .......
# import math
#
# print(math.sqrt(49))

# import datetime
#
# # A--> day of the week
# # B --> month of year
# print(datetime.datetime.now().strftime("%a"))
# print(datetime.datetime(2023, 9, 15))
