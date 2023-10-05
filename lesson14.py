
# # 2. mydict = {
# #         '1': 'Lesson',
# #         '2': 'Lesson2',
# #         '3': 'Lesson3',
# # }
# # myNewdict = {}
# # Bu dictionary-nin elementlərini dövr operatoru vasitəsilə myNewdict-ə əlavə edən funksiya yazın.



# # mydict = {
# #         1: 'Lesson',
# #         2: 'Lesson2',
# #         3: 'Lesson3',
# # }

# # myNewdict = {}


# # for key in mydict.keys(): #[1,2,3]
# #     for value in mydict.values(): #[Lesson, Lesson2, Lesson3]
# #         myNewdict.update({key:value})
# # print(myNewdict)

# # 4. İstifadəçi float tip bir ədəd daxil edəcək.
# # Bu ədddə vergüldən sonrakı hissənin rəqəmlərini bir list-ə əlavə edən funksiya yazın.


# # eded = float(input("Ededi daxil edin: ")) # 8.55786 -- > '8.55786' --> ['8', '55786']

# # def myfunc(eded):
# #     newlist = []
# #     str_eded = str(eded).split(".")
# #     second_part = str_eded[1]
# #     for i in second_part:
# #         newlist.append(i)
# #     newlist = list(map(int, newlist))
# #     return newlist
# # print(myfunc(eded))
# # #8.5


# # 5. Daxil edilən sözdə ə, ı, ü, ş, ç, ğ olduğu zaman onları 
# # ingilis hərfi ilə əvəz edən funksiya yazın.


# # soz = input("Sozu daxil edin: ")

# # def myfunc(soz):
# #     for i in range(len(soz)): #salam -- >  for i in soz: 
# #         if soz[i] == 'ə':
# #             soz = soz.replace(soz[i], "a")
        
# #         if soz[i] == "ü":
# #             soz = soz.replace(soz[i], "u")
           
# #     return soz


# # print(myfunc(soz))
# # soz = input("sozu daxil edin: ") # əleykim
# # mylist = []
# # az_elifba = ['ə','ü', 'ı', 'ğ', 'ö', 'ç', 'ş']

# # for i in range(97,123):
# #     mylist.append(chr(i))
# # print(mylist)
# # for i in soz:
# #     if i in az_elifba:
# #         if i == 'ə':
# #             soz = soz.replace(i, 'a')
# #         if i == 'ü':
# #             soz = soz.replace(i, 'u')
# #         if i == 'ı':
# #             soz = soz.replace(i, 'i')
# # print(soz)



# # x = 5   # global tip deyisen

# # print(x)


# # def salamla():
# #     y = 5   # local deyisendir.

# #     def sagol():
# #         nonlocal y
# #         y = 3
    
# #     sagol()
# #     print(y)

# # salamla()




# # -- > read, write.

# # open file in current directory
# # file1 = open("test.txt")

# # file1.close()
# # print("salam\nsagol")

# # print(file1.readlines())

# # -- r,w,a

# with open("test.txt", "r+") as file1:
#     print(file1.readline())
#     file1.write("\nEstoniya")





sentence = input("Enter the sentence: ")
my_dict = {}


for i in sentence:
    my_dict.update({i:sentence.count(i)})

sorted_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1], reverse=True)}

top_5_dict = dict(list(sorted_dict.items())[:5])

print(top_5_dict)



