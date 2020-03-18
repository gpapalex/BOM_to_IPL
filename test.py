# print the current working directory
# cwd = print(os.getcwd())
# changes the working directory
# os.chdir("C:\Users\Papalexandropoulos\Desktop\General\Workspace")
# ls -all
# os.listdir('.')
# Works only on windows paths
# df = pd.read_excel('C:/Users/Papalexandropoulos/Desktop/General/Workspace/BOM_Example/624I60026-120_BOM.xlsx')

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


file_to_open = Path(
    r'C:/Users/Papalexandropoulos/Desktop/General/Workspace/BOM_Example/624I60026-120_BOM.xlsx')

# excel_file = "624I60026-120_BOM.xlsx"
df = pd.read_excel(file_to_open, sheet_name='624I60026-120')


class separation:
    idnumber = []
    name = []
    combined = df['Object description'].tolist()


class fixing_explvl:
    expl_column = df['Explosion level']
    # passing values from column explosion level to a list
    mylist = df['Explosion level'].tolist()
    x = -1
    for listvalues in mylist:
        x += 1
        temp_list = listvalues.split(".")
        for i in temp_list:
            if i.isdigit():
                mylist[x] = int(i) - 2


# Saving changes
# df.to_excel("OBM_Fixed.xlsx")
