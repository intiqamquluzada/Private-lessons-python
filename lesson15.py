# 2. Daxil edilən cümlənin özündə deyil, hər bir
# sözündə təkrarlanan hərfləri bir str-e elave eden.
# Məsələn cümlə belədirsə:
# Salam dərsimiz başladı --> Salm dərsimz başldı
# bu şəkildə olmalıdır.
import random

# cumle = input("Cumleni daxil edin: ").split()
# def no_repeat(sentence):  # Salam ders basladi -- > ['Salam', 'ders', 'basladi']
#     mystr = ""
#     for i in range(len(sentence)):  # i = 0,1,2
#         for j in range(len(sentence[i])):  # j = 0,1,2,3,4
#             if sentence[i].count(sentence[i][j]) > 1:  # salam.count(S) > 1
#                 mystr += sentence[i][j]
#
#     return mystr
#
#
# print(no_repeat(cumle))



# 3. Daxil edilən ədədin sadəliyini yoxlayan funksiya yazın
# (əvvəlki misallara baxmayın, özünüz yazmağa cəhd edin
# , sadə ədəd yalnız 1ə və özünə bölünən ədəddir).


# eded = int(input("Ededi daxil edin: "))

# Sade eded 1-e ve yalniz ozune. --> 11,13,43


# yoxlamaliyiq 2den edede qeder her hansi bir edede bolunurmu
# def sade_eded(num):
#     for i in range(2,num):
#         if num % i == 0:
#             return "Murekkeb ededdir"
#     else:
#         return "Sadedir"
#
# print(sade_eded(eded))


# 4. Daxil edilən 2 ədədin cəminin fərqindən
# neçə dəfə böyük olduğunu qaytaran funksiya yazın.


# eded1 = int(input("eded-1: "))
# eded2 = int(input("eded-2: "))


# def myfunc(num1,num2):
#     return (num1 + num2) // (num1-num2)
#
# print(myfunc(eded1,eded2))



# num1 = int(input("Eded1- "))
# num2 = int(input("Eded2- "))
# num3 = int(input("Eded3- "))
#
#
# 7,5,6,6
# if num1 >= num2 >= num3 or num1 >= num3 >= num2:
#     print(num1)
# elif num2 >= num1 >= num3 or num2 >= num3 >= num1:
#     print(num2)
# elif num3 >= num1 >= num2 or num3 >= num2 >= num1:
#     print(num3)




#-------------------------------
# num1 = int(input("1-ci ededi daxil edin: "))
# num2 = int(input("2-ci ededi daxil edin: "))
# num3 = int(input("3-cu ededi daxil edin: "))
#
#
# if num1 > num2 and num1 > num3:
#     print(num1)
# elif num2 > num1 and num2 > num3:
#     print(num2)
# elif num3 > num1 and num3 > num2:
#     print(num3)

# 6. 2lik və 10luq say sistemlərini araşdırın.
# 2lik say sistemindən 10 luq say sisteminə necə keçirilir və
# 10luq say sistemindən 2lik say sisteminə necə keçirilir.
# Bunu tam dərk etdikdən sonra istifadəçidən aldığınız ədədi
# 2lik say sisteminə keçirən funskiya yazmağa cəhd edin.
# 123 -- > 1010101010

# -----------------------------------------------------------
# GELEN DERS BAXAQ




# num dəyərinə random bir ədəd mənimsədin(1,100 aralığından).
# Və daha sonra istifadəçidən o ədədi tapmasını tələb edin,
# ədəddən yuxarı deyilərsə aşağı düş, aşağı deyilərsə yuxarı qalx yazısı
# çap olunsun.
# Tapdıqda təbriklər çap olunsun. Bunlar baş verərkən proqram dayanmasın.



num = random.randint(1,100)
print(num)


while True:
    eded = int(input("Ededi tapin: "))

    if eded > num:
        print("Asagi dusun")
    elif eded < num:
        print("Yuxari qalx")
    else:
        print("Siz tapdiniz")
        break















