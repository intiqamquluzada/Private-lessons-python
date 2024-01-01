#import random

# 4. Istifadeci muxtelif herfler daxil edecek
# ve bu herflerden random sozler duzelden funksiya yazin.

# herfler = input("Herfleri daxil edin: ").split()



# random.shuffle(herfler)
# # x = random.choice(herfler)
# mystr = "".join(herfler)


# print(mystr)


# for i in range(1,100):
#     print(i)
#
# i = 1
# while i < 100:
#     print(i)

# mylist = [1.5,6,'a','s']

# for i in mylist:
#     print(i)
#
# for i in range(len(mylist)):
#     print(mylist[i])

# i = 0
# while i < len(mylist): # 0,1,2,3
#     print(mylist[i])
#     i = i + 1


# 4. While dovr operatoru vasitesile iki ededin hasilini hesablayin.
eded1 = int(input("1ci ededi daxil edin: ")) # 5
eded2 = int(input("2ci ededi daxil edin: ")) # 4
# 5x4 = 4 + 4 + 4 + 4 + 4
cem = 0
i = 0
while i < eded1:
    cem += eded2
    i = i + 1
print(cem)





