#PYTHONDA funksiyalar

# def toplama():
#     return 5

# print(toplama())


# def cumle_qaytaran():
#     return "Salam funksiya isledi"

# cumle_qaytaran()

# def ededi_goster(eded): #parametr
#     return eded

# print(ededi_goster(67))
# ededi_goster(100)


# def toplama(eded1,eded2):
#     return eded1 + eded2

# print(toplama(3,4))


# def cumle_duzelden(ad, soyad):
#     return ad + " " + soyad

# print(cumle_duzelden("Intigam", "Guluzade"))


# def ad_soyad(ad, soyad):
#     return ad + " " + soyad


# print(ad_soyad("Guluzade", "Intigam"))
# print(ad_soyad(soyad='Guluzade', ad='Intigam'))




# def ilk_herf_gosteren(soz='Alma'):
#     return soz[0]

# print(ilk_herf_gosteren())



# def show_list_elements(mylst):
#     for i in mylst:
#         print(i)



# menim_list = [1,2,3,4,3,2,2,2]

# show_list_elements(menim_list)


# def toplama(x,y):
#     pass



# *args ve **kwargs   -->  args = list,tuple;   kwargs = dict 


# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus", "Intigam", "Fateh")



# def myfunc(eded1,eded2):
#     return eded1 + eded2

# print(myfunc(3,4,5))


# **kwargs
# def my_function(**kid): # key, value
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")


# kid = {
#   "fname": "Tobias",
#   "lname": "Refsnes"
# }

# mydict['ad'] --> Intigam

#DERSDE ISLENILEN TAPSIRIQLAR


# Istifadeciden 2 eded alin ve onlarin hasilini qaytaran funksiya yazin.
# +




# Istifadeciden 2 eded alin ve hansi boyukdurse onu qaytaran funksiya yazin.

# num1 = int(input("1ci ededi daxil edin: "))
# num2 = int(input("2ci ededi daxil edin: "))


# def is_bigger(eded_1, eded_2):
#     if eded_1 > eded_2:
#         return eded_1
#     else:
#         return eded_2

# print(is_bigger(num1,num2))



# Daxil edilen cumlenin uzunlugunu qaytaran funksiya yazin
# soz = input("sozu daxil edin:" )
# def len_soz(soz):
#     return len(soz)


# print(len_soz(soz))




# Daxil edilen sozun tersini qaytaran funksiya yazmaga cehd edin.


# eded = input("ededi daxil edin:" )
# def reverse_num(eded):
#     return eded[::-1]
#     # return int("".join(list(reversed(eded))))
# print(reverse_num(eded))








# Ededin tek yaxud cut oldugunu qaytaran funksiya yazin.

# eded = 8
# def boyuk_eded(eded):
#     if eded % 2 == 0:
#         return "cutdur"
#     else:
#         return "tekdir"

# a = boyuk_eded(eded)
# print(type(a))


# Istifadeciden bir list alin ve bu list-in elementlerini cap eden funksiya yazin.

# user_list= input("ededi daxil edin:" ).split()

# def print_list(user_list):
#     for i in user_list:
#         print(i)
# print(print_list(user_list))

# user_list= input("ededi daxil edin:" ).split()
# for i in user_list:
#  def print_list(user_list):
#     return user_list[i]
# print(print_list(user_list))




# Istifadeciden bir list alin ve bu list-in elementlerinin cemini qaytaran funksiya yazin. (istifadeci ancaq
# eded daxil edecek)


# my_list = input("daxil edin: ").split()


# my_list = list(map(int, my_list))


# def sum_list(my_list):
#     return sum(my_list)
# print(sum_list(my_list))


# Daxil edilen ededin reqemlerini ekrana cap eden funksiya yazin.


# user_list= input("ededi daxil edin:" )
# # '468' -- > 4,6,8

# def print_list(user_list):
#         for i in user_list:
                
#             print(int(i))
# print_list(user_list)



# Daxil edilen cumledeki sozlerin bas herfini ekrana cap eden funksiya yazin.



# cumle = input("Cumleni daxil edin : ").split()


# def bas_herf(cml):
#     for i in cml:
#         print(i[0])

        
# bas_herf(cumle)















