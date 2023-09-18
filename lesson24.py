# 2. Bir Area adlı class yaradın. Və bundan törəmə Square, Triangle, Circle classları olsun.
# Atributları və metodları öz düşüncənizə uyğun yazın. (Polimorfizm anlayışından istifadə edin.)

# class Figure:
#     def __init__(self, side):
#         self.side = side
#
#     def __str__(self):
#         self.side

# class Square(Figure):
#     def __init__(self, side):
#         super().__init__(side)
#
#     def perimeter(self):
#         return self.side * 4
#
#     def area(self):
#         return self.side ** 2
#
# class Triangle(Figure):
#     def __init__(self, side, side2, side3, height):
#         super().__init__(side)
#         self.height = height
#         self.side2 = side2
#         self.side3 = side3
#
#     def __str__(self):
#         return self.height
#
#     def perimeter(self):
#         return self.side + self.side2 + self.side3
#
#     def area(self):
#         return (1 / 2) * self.side * self.height
#
# class Circle(Figure):
#     def __init__(self, side, pi):
#         super().__init__(side)
#         self.pi = 3.14
#
#     def __str__(self):
#         return self.side
#
#     def area(self):
#         return self.pi * self.side ** 2
#
#     def length(self):
#         return 2*self.pi*self.side


# bir deyisen yaxud bir metod bir ad altinda muxtelif yerlerde muxtelif is gorurse bu anlayisa
# polimorfizm deyilir


# 8. MyCard deyə bir class yaratmalısınız. username, balance, pin_code atributlarını verin.
# Daha sonra get_cash() deyə bir metod yaradın, hansı ki, bu metodu çağıranda bizdən məbləğ istəsin,
# əgər balansdakı puldan çox deyilsə, pin_code-ni istəsin, doğru olduğu halda həmin məbləği balansdan
# çıxarsın və "Uğurlu əməliyyat, balansınız: (balansda qalan pul)".
# Həmçini in_cash() deyə bir metod yazın, istifadəçidən məbləğ istəyin, daha sonra pin_codeni istəyin,
# pin_code doğru olarsa, həmin məbləği balansla toplayın, balansımız o olsun. Birdənə də send_money()
# metodu yazın. Bu metodu da işə saldıqda  16 rəqəmli kart nömrəsi istəyin. Əgər daxil edilənlərdən
# hamısı rəqəmdirsə və 16 rəqəmlidirsə, köçürüləcək məbləği istəyin. Köçürüləcək məbləğ
# balansdan çox olmadığı təqdirdə balansdan həmin məbləği çıxın və "Uğurlu köçürülmə" return etsin.


# class MyCard:
#     def __init__(self, username, balance, pin_code, quantity):
#         self.username = username
#         self.balance = balance
#         self.pin_code = pin_code
#         self.quantity = quantity
#
#     def __str__(self):
#         return f"{self.username}/{self.balance}"
#
#     def get_cash(self):
#
#         if self.quantity <= self.balance:
#             pin_code = input("Enter the pin code: ")
#             if pin_code == self.pin_code:
#                 self.balance = self.balance - self.quantity
#                 return f"Success, balance: {self.balance}"
#             else:
#                 return "Pin code is wrong"
#         else:
#             return "Balance is not enough to out"
#
#     def in_cash(self):
#         pin_code = input("Enter the pin code: ")
#         if pin_code == self.pin_code:
#             self.balance += self.quantity
#             return f"Success, balance: {self.balance}"
#         else:
#             return "Wrong pin code"
#
#     def send_money(self):
#         card_number = input("Enter the 16 numbers of your card: ")
#         if card_number.isdigit():
#             if len(card_number) == 16:
#                 send_money = int(input("Enter value: "))
#                 if send_money <= self.balance:
#                     self.balance -= send_money
#                     return f"Success, balance:{self.balance}"
#
#                 else:
#                     return "Not enough balance"
#             else:
#                 return "Card numbers are wrong"
#         else:
#             return "Card numbers are wrong(has alphabetic elements)"


# card1 = MyCard(username="intigam", balance=15, pin_code="1234", quantity=20)

# print(card1.get_cash())
# print(card1.in_cash())
# print(card1.send_money())


# class Animal:
#     def __init__(self,color, weight):
#         self.__color = color
#         self.__weight = weight
#
#     def __str__(self):
#         return f"{self.__color}/{self.__weight}"
#
# obj1 = Animal(color='Yellow', weight=200)
#
# print(obj1.color, obj1.__color)




# class Animal:
#     def __init__(self, age):
#         self.age = age
#
#     def __str__(self):
#         return self.age
#
#     def __sound(self):
#         return "Hello"
#
# obj1 = Animal(age=4)
# print(obj1.sound())








