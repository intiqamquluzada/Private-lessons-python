# Daxil edilən 2 ədəd arasındaki sözlərin ASCİİ qarşılıqlarını bir list-ə əlavə edin.
# (While dövr operatoru ilə)
# num1 = int(input("1ci ededi daxil edin: "))
# num2 = int(input("2ci ededi daxil edin: "))
# newList = []
# i = num1
# while i < num2:
#     newList.append(chr(i))
#     i += 1
# print(newList)


# 5. İstifadəçidən müxtəlif hərflər alın.
# Daha sonra bu herfleri əlifba sırasına görə düzüb, birləşdirin. (While dövr operatoru ilə)
# herfler = input("Herfleri daxil edin: ").split()
# herfler.sort()
# mystr = ""
# i = 0
# while i < len(herfler):
#     mystr += herfler[i]
#     i += 1
# print(mystr)

# 4. İstifadəçidən bir söz alın əgər sait hərflərin sayı çoxdursa, "saitlər qalib gəldi",
# bərabərdirsə "bərabər",
# samitlər çox olduğu halda "samitlər qalib gəldi" çap edin. (While dövr operatoru ilə)


# word = input("Sozu daxil edin: ")
# saitler = ['a', 'e', 'i', 'u', 'o']
# sait_count = 0
# samit_count = 0
# i = 0
# while i < len(word):
#     if word[i] in saitler:
#         sait_count +=1
#     else:
#         samit_count+=1
#     i+=1
#
# if sait_count > samit_count:
#     print("Saitler qalib geldi")
# elif sait_count < samit_count:
#     print("Samitler qalib geldi")
# else:
#     print("Beraber say")


# 10. Üçbucaq, kvadrat, çevrə. Bunların sahəsini hesablayan funskiya yazın.
# Məsələn, funksiya işə düşdükdə bu 3 fiqurun adları görünsün. Hər hansı biri seçilərsə,
# ona uyğun sahəni hesablamaq üçün parametrlər soruşulsun və nəticə hesablanıb return edilsin.
# def triangle(a, h):
#     return (1 / 2) * a * h
# def square(a):
#     return a ** 2
# def circle(r):
#     pi = 3
#     return pi * (r ** 2)
#
# def area_calculator():
#     figure = input("Which figure ?\n 1.Triangle\n2.Square\n3.Circle\n:")
#     if figure == "1":
#         side = int(input("Enter the main side: "))
#         height = int(input("Enter the height of triangle: "))
#         return triangle(side, height)
#     elif figure == "2":
#         side = int(input("Enter the any side of square: "))
#         return square(side)
#     elif figure == "3":
#         radius = int(input("Enter the radius of the circle: "))
#         return circle(radius)
#     else:
#         return "Wrong operation"
# print(area_calculator())


# OOP - Object Oriented Programming --> az. OYP --> Obyekt Yonumlu Proqramlasdirma

# class Person:
#     yas = 5
# p = Person()
# p5 = Person()

# print(p.yas, p5.yas)


# class Animal:
#     def __init__(self, color, age):
#         self.color = color
#         self.age = age
#
#
# cat = Animal(color='white', age=1)
# dog = Animal(color='brown', age=2)
#
# print(cat.color, cat.age)
# print(dog.color, dog.age)


# class Vehicle:
#     def __init__(self, color, energy_type):
#         self.color = color
#         self.energy_type = energy_type
#
#     def __str__(self):
#         return self.color + "->" + self.energy_type
#
# car = Vehicle(color='black', energy_type='gasoline')
# print(car)


# class Electronics:
#     def __init__(myself, condition, color):
#         myself.condition = condition
#         myself.color = color
#     def __str__(myself):
#         return myself.condition
# wash_machine = Electronics(condition="New", color="Gray")
# print(wash_machine)


# class Animal:
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#
#     def __str__(self):
#         return self.name + "," + str(self.age) + ","
#
# cat = Animal(name="Mestan", age=1, color='gray')
# dog = Animal(name='Husky', age=2, color='black')
#
# del cat.color
# dog.age = 5
#
# print(cat)
# print(dog)
# class Person:
#     pass