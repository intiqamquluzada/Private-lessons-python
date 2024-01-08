# 7. Daxil edilen sozun son herfini 10 defe ozu ile birlesdiren funksiya yazin.


# salam + 10*m



# soz = input("Sozu daxil edin; ")

# def last_letter(word):
#     return word + 10 * word[-1] 

# print(last_letter(soz))

# 10. Ele bir funksiya yazin ki, parol = "Estoniya" olsun. 
# Ve istifadeci bu parolu tapana qeder proqram dayanmasin.




# def find_password():
#     parol = "Estoniya"
#     while True:
#         password = input("Parolu daxil et: ")

#         if password.lower() == parol.lower(): 
#             print("Siz tapdiniz")
#             break

# find_password()


# def find_password():
#     while True:
#         password = input("Parolu daxil edin: ")
#         if "Estoniya" in password: #SalamEstoniya
#             print("Siz tapdiniz")
#             break
# find_password()



# 11. Daxil edilen cumleni bir str tipi kimi birlesdirib 
# yeniden "i" herfine gore bolen bir funksiya yazin.


# Salam necesiz ne var ne yox 
# Salamnecesi znevarneyox

# cumle = input("Cumleni daxil edin : ")
# Salam necesiz ne var ne yox -- > ['Salam', 'necesiz', ...]


# def myfunc(sentence):
#     sentence = sentence.split()
#     sentence = "".join(sentence) # Salamnecesiznevarneyox
#     sentence = sentence.split("i")
#     return sentence

# print(myfunc(cumle))


# def myfunc():
#     return 4 + 5

# print(myfunc())

# 13. Daxil edilen ededden 100 vahid geride ve 100 vahid irelide duran cut ededleri 
# bir list-e elave eden funksiya yazin.

# eded = int(input("ededi daxil edin: "))

# def myfunc(number):
#     newlist = []
#     if number > 100:
#         for i in range(number - 100, number + 101):
#             if i % 2 == 0:
#                 newlist.append(i)
#     print(newlist)

# myfunc(eded)


# soz =  input("sozu daxil edin: ") # 'salam' --> 'salam',   's','a','l','a','m'



# def my_func(soz):
#     newlist = []
#     for i in soz:
#         newlist.append(i)

#     for i in range(len(newlist)):
#         if newlist[i] == "a" or newlist[i] == 'A':
#             newlist[i] = "i"
#     return "".join(newlist)
# print(my_func(soz))



