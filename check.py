""""
temp_name = ['XL_OHSC','4F+','LH','PC']
for i in range(len(temp_name)):
   name = ' '.join(temp_name)

print(name)
"""
name = []
idnumber = []
general = []


def splition(word):
    return[char for char in word]


general = "RIVET_AD32ABS"
flag = True
seperate = splition(general[])
if len(general) == 0 and flag == True:  # check in case of ex.RIVET_AD32ABS
    for x in range(len(seperate)):
        if "_" or "-" == seperate[x]:
            name.append(seperate[:x-1])
            idnumber.append(seperate[x+1:len(seperate)])

len(general) == 0 and flag == True:  # check in case of ex.RIVET_AD32ABS
    for x in range(len(seperate)):
        if "_" or "-" == seperate[x]:
            name.append(seperate[:x-1])
            idnumber.append(seperate[x+1:len(seperate)])

print(name)
print(idnumber)
print(seperate)
print(general)
