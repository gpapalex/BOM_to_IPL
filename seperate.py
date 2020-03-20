import os
import pandas as pd
import numpy as np
from pathlib import Path


file_to_open = Path(
    r'C:/Users/Papalexandropoulos/Desktop/General/Workspace/BOM_Example/624I60026-120_BOM.xlsx')


# excel_file = "624I60026-120_BOM.xlsx"
df = pd.read_excel(file_to_open, sheet_name='624I60026-120')


def splition(word):
    return[char for char in word]


idnumber = []
name = []
combined = df['Object description'].tolist()


for k in range(len(combined)):  # looping through each item in objdesc column
    # split each column value and store it to a general list
    general = combined[k].split()  # split each shell value where every space
    num_freq = 0
    letter_freq = 0
    fol = 0
    flag = True
    if len(general) == 1:
        prev_name = []  # krataei to proigoymeno string an einai onoma
        prev_num = []  # krataei to proigoymeno string an einai arithmos
        temp_list = []  # kratei se diaforetika string kathe ti apo - kai _
        hold = []  # krataei to position gia kathe - kai _
        flag_f = True
        seperate = splition(general)
        pos = -1
        for y in range(len(seperate)):  # loop through each ch on the list
            if (seperate[y] == "_" or seperate[y] == "-"):
                pos += 1
                hold[pos] = y
        for y in range(len(hold)):
            if y == 0:
                temp_list.append(general(: hold[y]))
            elif y == len(hold):
                temp_list.append(general(hold[y]: len(seperate)))
            else:
                temp_list.append(general(hold[y]: hold[y+1]))

        if len(temp_list) == 2:
            num_freq1 = 0
            num_freq2 = 0
            seperate1 = splition(temp_list[0])
            seperate2 = splition(temp_list[1])
            for i in range(len(seperate1)):
                if seperate1[i].isdigit():
                    num_freq1 += 1
            for i in range(len(seperate2)):
                if seperate2[i].isdigit():
                    num_freq2 += 1
            if num_freq1 > num_freq2:
                idnumber.append(temp_list[0])
                name.append(temp_list[1])
            else:
                idnumber.append(temp_list[1])
                name.append(temp_list[0])
        else:
            num_freq_list = []

            for y in range(len(temp_list)):
                seperate_loc = splition(temp_list[y])
                num_freq_loc = 0
                alpha_freq_loc = 0
                for f in range(len(seperate_loc)):
                    if seperate_loc[f].isdigit():
                        num_freq_loc += 1
                    elif seperate_loc[f].isalpha():
                        alpha_freq_loc += 1
                if len(seperate_loc) == num_freq_loc:
                    prev_num.append(temp_list[y])
                elif len(seperate_loc) == alpha_freq_loc:
                    prev_name.append(temp_list[y])
                else:
                    if((num_freq_loc >= len(temp_list[y]) or (num_freq_loc >= 1)):
                        if((len(prev_name) == 0) and (len(prev_num) == 0)):
                            # checks if previous and next exists
                            if(((y - 1) >= 0) and ((y + 1) <= len(temp_list))) == True:
                                prev1=splition(temp_list[y-1])
                                next1=splition(temp_list[y+1])
                                flag1_top=False
                                met1=0
                                met2=0
                                for i in range(len(temp_list[y-1]])):
                                    if(prev1[i].isalpha()):
                                        met1 += 1
                                for i in range(len(temp_list[y+1])):
                                    if( next1[i].isalpha() ):
                                        met2 += 1

                                if( (met1 == len(prev1)) and (met2 == len(next1)) ):
                                    flag1_top = True
                                if( flag1_top  ):
                                    name.append(temp_list[y])
                                else:
                                    idnumber.append(temp_list[y])
                            prev_num.append(temp_list[y])
                        else:
                            idnumber.append(temp_list[y])

                    else:
                        name.append(temp_list[y])
                        (len(prev_num)=0)
                        prev_name.append(temp_list[y])

    else:
        for i in range(len(general)):
            # split each ch on another list called seperate
            seperate = splition(general[i])
            for y in range(len(seperate)):  # loop through each ch on the list

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
                                    name_ins = ''.join(
                                        seperate[y+2:len(seperate)])
                                    idnumber.append(idnum_ins)
                                    temp_name.append(name_ins)
                                    flag = False
                                    break
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

