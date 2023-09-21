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


myHashed = "XFQFR"
myHashed = myHashed.lower()
print(myHashed)
newlist = ""
for j in range(1, 27):
    for i in range(len(myHashed)):
        if mlist.index(myHashed[i]) + j <= 26:
            newlist += mlist[mlist.index(myHashed[i]) + j]
    else:
        if i + j -26 != 0:
            newlist += mlist[i+j-26]
        else:
            newlist += mlist[i + j - 25]

for i in range(len(newlist)):
    if i == 5:
        mystr =
print(newlist)
