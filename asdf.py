value = "624I60026-120 XL OHSC 4F+ LH PC"
value2 = "624A10145-012_CUT EDGE_PROT_BIN_LIP"
value4 = "624I60026-120_XL_OHSC 4F+ LH PC"


def split(word):
    return[char for char in word]


idnumber = []
name = []
seperate = split(value5)
fo = 0
num_freq = 0


for y in range(len(seperate)):
    if seperate[y].isdigit():
        fo += 1
        if fo >= 2:
            if len(seperate) = y:
                if (seperate[y+1] == "-" or seperate[y+1] == "_") == True:
                    if seperate[y+2].isalpha() == True:
                        # check if  D252-73810-202_CL._TUBE_SUPPORT_EL. split and D252-73810-202_ goes to idnumber list
                        idnumber.append(seperate[:y+1])
                        # check if  D252-73810-202_CL._TUBE_SUPPORT_EL. split and CL._TUBE_SUPPORT_EL goes to name list
                        name.append(seperate[y+2:len(seperate)])
                        break

"""if num_freq >= int((len(seperate) / 2)):
            if len(seperate) >= 5:
                idnumber.append(general[i])
            else:
                name.append(general[i])
        else:
            if general[i].startswith("("):
                idnumber.append(general[i])
            else:
                name.append(general[i])"""


"""

idnumber = []
name = []


def splition(word):
    return[char for char in word]

combined = df['Object description'].tolist()
for k in range(len(combined)): # looping through each item in objdesc column
    general = combined[k].split() # split each column value and store it to a general list
    for i in range(len(general)): # loop through each value in list we splited
        num_freq = 0
        fol = 0
        seperate = splition(general[i]) # split on anathoer list each ch through a function splition
        for y in range(len(seperate)): # loop through each ch on the list            
            if seperate[y].isdigit():
                num_freq += 1 # number frequence in each value on the seperated list of each ch
                fol += 1
                if fol >= 2:
                    if (seperate[y+1] == "-" or seperate[y+1] == "_") == True:
                        if seperate[y+2].isalpha() == True:
                            idnumber.append(seperate[:y+1]) # check if  D252-73810-202_CL._TUBE_SUPPORT_EL. split and D252-73810-202_ goes to idnumber list
                            name.append(seperate[y+2:len(seperate)]) # check if  D252-73810-202_CL._TUBE_SUPPORT_EL. split and CL._TUBE_SUPPORT_EL goes to name list
                            break 
                                                                 
        if num_freq >= int((len(seperate) / 2)):
            if len(seperate) >= 5:
                idnumber.append(general[i])
            else:
                name.append(general[i])
        else:
            if general[i].startswith("("):
                idnumber.append(general[i])
            else:
                name.append(general[i])"""
print(idnumber)
print(name)
print(seperate)
