# mylist = [1, 2, 3, 4, 5, 6]
# i = 0
# while i < len(mylist):
#
#     if mylist[i] == 5:
#         continue
#     print(mylist[i])
#     i = i + 1

# mylist = [1, 2, 3, 4, 5, 6]
# i = 0
# while i < len(mylist):
#     if mylist[i] == 5:
#         i = i + 1  # Eğer eleman 5 ise i'yi artır, aksi takdirde döngüyü sonsuz yapar.
#         continue
#     print(mylist[i])
#     i = i + 1


# eded = input("deyrleri daxil edin: ").split()
# i =0
# while i<len(eded):
#     if eded[i].isdigit() and int(eded[i]) % 2 == 0:
#
#         print(i)
#     i+=1


# nums = input("ededleri daxil edin: ")
# cem = 0
# for i in nums:
#         cem += int(nums[i])
# if cem % 2 == 0:
#         print("ededler cutdur")
# else:
#         print("tekdir")


# 11.Verilmiş ədədin tərsini çap edin(while ile edin, reversed yaxud [::-1] ile etmeyin)

# num = int(input("Ededi daxil edin: "))  # -- > 231 -->
# 231 -- > 231 % 10 = 1 --> 231 // 10 = 23 % 10 --> 3 --> ....

# mystr = ""
# qaliq = 0
# for i in range(len(str(num))):  # '231' = 3 defe
#     qaliq = num % 10  # 1, 3
#     mystr += str(qaliq)  # '1' + '3' = '13' -- > '132'
#     num = num // 10  # 23
# print(mystr)
# print(5 == 7)


# 20. mylist = ['a', 1,-5,78,9,0,'alma', 10]
# Elə edin ki, bu list-də yalnlz ədəd tipdə olan elementlər qalsın
# və onlar azdan çoxa doğru artsın.

# mylist = ['a', 1, -5, 78, 9, 0, 'alma', 10]
# newlist = []
# for i in range(0, len(mylist)):
#     if type(mylist[i]) == type(50):
#         newlist.append(mylist[i])


# mylist = newlist.copy()
# print(mylist)
