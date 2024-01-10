# S.O.L.I.D principles

# Single Responsibility Principle

# IGNORED
# class Book:
#     def __init__(self, title, author, year, content):
#         self.title = title
#         self.author = author
#         self.year = year
#         self.content = content
#     def replaceWordInContent(self,word):
#         self.content = self.content.replace(self.content, word)
#         return self.content
#     def printBook(self):
#         print(self.content)


#------------------------------------------------------


# Accepted
# class Book(object):
#     def __init__(self, title, author, year, content):
#         self.title = title
#         self.author = author
#         self.year = year
#         self.content = content
#
#     def replaceWordInContent(self, word: str) -> str:
#         self.content = self.content.replace(self.content, word)
#         return self.content
#
#
# class Printer:
#     def __init__(self, book: Book):
#         self.book = book
#
#     def printBook(self):
#         print(self.book.content)

# 2. OPEN/CLOSED principle -- > kod deyisdirilmeye bagli, genislendirmeye aciq olmalidir
# class Discount:
#     def __init__(self, customer, price):
#         self.customer = customer
#         self.price = price
#     def give_discount(self):
#         return self.price * 0.1
#
# class DiscountForGoldUsers(Discount):
#     def get_discount(self):
#         return super().give_discount() * 5



#--------------------------------------------------------


# 3. Liskov Substitution Principle
# A class --> parent
# B class --> child

# B classinin islene bildiyi her yerde A classi da islene bilmelidir.

# class Animal:
#     def __init__(self, food):
#         self.food = food
#
#
# class Dog(Animal):
#     def __init__(self, food):
#         super().__init__(food)
#         self.food = food
#
#
# class Cat(Animal):
#     def __init__(self, food):
#         super().__init__(food)
#         self.food = food
#
#
# toplan = Dog("bones")
# mestan = Cat("whiskas")
#
#
# def FeedTheAnimal(animal: Animal):
#     print(type(animal))
#     message = "You feed the " + str(type(animal).__name__) + " with " + animal.food
#     print(message)
#
#
# FeedTheAnimal(toplan)
# # FeedTheAnimal(mestan)


#----------------------------------------------------------------------

# 4. Interface Segregation

# class IShape:
#     def draw_circle(self): print("Daire cekildi")
#
#     def draw_rectangle(self): print("Ucbucaq cekildi")
#
#     def draw_square(self): print("Kvadrat cekildi")
#
#
# class IShape:
#     def draw(self):
#         raise NotImplementedError
#
#
# class Circle(IShape):
#     def draw(self):  # OVERRIDE
#         print("Draw circle")
#
#
# class Rectangle(IShape):
#     def draw(self):
#         print("Draw rectangle")
#
#
# class Square(IShape):
#     def draw(self):
#         print("Draw square")


#---------------------------------------------------------------------



# 5. Dependency Inversion Principle
# IGNORED

# class Production:
#     def produce(self):
#         bread = Bread()
#         bread.bake(True)
#
# class Bread:
#     def bake(self, isTendir: bool):
#         print("Bread was baked in tendir")


# ACCEPTED
# class IFood:
#     def bake(self): pass
#
# class Bread(IFood):
#     def bake(self):
#         print("Bread was baked")
# # test üçün bir class daha əlavə edirəm, etməsək də olar
#
# class Pastry(IFood):
#     def bake(self):
#         print("Pastry was baked")
#
# class Production:
#     def __init__(self, food): # food burada IFood interfeysini implement edən hər hansı bir class olacaq
#         self.food = food
#
#     def produce(self):
#         self.food.bake()
