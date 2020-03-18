import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


file_to_open = Path(
    r'C:/Users/Papalexandropoulos/Desktop/General/Workspace/BOM_Example/624I60026-120_BOM.xlsx')

# excel_file = "624I60026-120_BOM.xlsx"
df = pd.read_excel(file_to_open, sheet_name='624I60026-120')


idnumber = []
name = []


def splition(word):
    return[char for char in word]


combined = df['Object description'].tolist()
for k in range(len(combined)):  # looping through each item in objdesc column
    # split each column value and store it to a general list
    general = combined[k].split()
    temp_name = []
    for i in range(len(general)):  # loop through each value in list we splited
        num_freq = 0
        fol = 0
        flag = True
        # split on anathoer list each ch through a function splition
        seperate = splition(general[i])
        for y in range(len(seperate)):  # loop through each ch on the list
            if seperate[y].isdigit():
                num_freq += 1  # number frequence in each value on the seperated list of each ch
                fol += 1
                if fol >= 2:
                    if len(seperate) > y + 1 and len(seperate) > y + 2:
                        if (seperate[y+1] == "-" or seperate[y+1] == "_") == True:
                            if seperate[y+2].isalpha() == True:
                                idnum_ins = ''.join(seperate[:y+1])
                                name_ins = ''.join(seperate[y+2:len(seperate)])
                                idnumber.append(idnum_ins)
                                temp_name.append(name_ins)
                                flag = False
                                break
                """elif len(general) == 0 and flag == True: #check in case of ex.RIVET_AD32ABS
                    for x in range(len(seperate)):
                        if "_" or "-" == seperate[x]:
                            name.append(seperate[:x-1])
                            idnumber.append(seperate[x+1:len(seperate)])"""

        if flag == True:
            if num_freq >= int((len(seperate) / 2)):
                if len(seperate) >= 5:
                    idnumber.append(general[i])
                else:
                    temp_name.append(general[i])
            else:
                if general[i].startswith("("):
                    general[i] = ""  # Setting blank every parenthesis
                else:
                    temp_name.append(general[i])

    for i in range(len(temp_name)):
        idname = ' '.join(temp_name)
    name.append(idname)
# for i in range(len(idnumber)):
 #   print(i, "-->", idnumber[i])

for i in range(len(name)):
    print(i, "-->", name[i])
# for i in range(len(name)):
 #   print(name[i])

print(len(idnumber))
print(len(name))
