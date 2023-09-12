# 29. Daxil edilen sozde boyuk herflerin sayini qaytaran funksiya yazin.


# sentence = input("Cumleni daxil edin; ").split()
#
# print(sentence)
# count = 0
# for i in sentence:
#     for j in i:
#         if j == j.upper():
#             count += 1
# print(count)



# 33.Daxil edilən sözün hərflərinin
# ASCİİ əlifbasındakı dəyərlərini bir list-ə əlavə edən funskiya yazın.

# word = input("Sozu daxil edin : ") #salam
# newlist = []
# for i in word:
#     newlist.append(ord(i))
# print(newlist)


# 34. İstifadəçi bir sətrdə boşluqlarla ədədlər daxil edəcək və
# ASCİİ dəyərlərinə uyğun gələn hərf
# və simvolları birləşmiş bir str tip dəyər şəklində return edən funskiya yazın.

# nums = input("Ededleri daxil edin: ").split()
# #['45','67','56']

# def myfunc(ededler):
#     ededler = list(map(int, ededler))
#     result = ""
#     for i in ededler:
#         result += chr(i)
#     return result
# print(myfunc(nums))
# nums = input("ededleri daxil edin: ").split()
# cem = 0
# count = 0
# for i in nums:
#     cem = 0
#     for j in i:
#         cem += int(j)
#     if cem % 2 == 0:
#         count += 1
# print(count)


