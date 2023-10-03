# soz = 'salam'
# key = 31
mlist = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
         'v', 'w', 'x', 'y', 'z']


# myHashed = ''
# for i in soz:
#     myvalue = mlist.index(i) + key
#     mymod = myvalue % 26
#     newletter = mlist[mymod]
#     myHashed += newletter
# print(myHashed)


class Car:
    def __init__(self, color, year):
        self.color = color
        self.year = year

    def __str__(self):
        return self.color


carclub = Car(color="----", year="----")


class SportCars(Car):
    def __init__(self, year, color, maxspeed):
        super().__init__(color, year)
        self.maxspeed = maxspeed

    def Carpower(self):
        return self.maxspeed

    def __str__(self):
        return self.maxspeed


car1 = SportCars(year="1976", color="red", maxspeed="320")

# class ClassicCars(Car):
#     def __init__(self, color, year, model, power):
#         super().__init__(color, year)
#         self.power = power
#         self.model = model
#
#     def Carpower(self):
#         return self.power
#
#     def __str__(self):
#         return self.power
#
#
# car2 = ClassicCars(color="white", year="1967", model="Sclass", power="340hp")
# print(car1)


# mystr = "kamaz"
# newstr = ""
# for i in range(len(mystr)):
#     newstr += mystr[i]
