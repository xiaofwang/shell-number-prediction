import pandas as pd
import numpy as np
import re

def composition(chem):
    list = re.findall(r'[A-Z][a-z]?\d*\.?\d*', chem)
    com_dic = {}
    for ls in list:
        match = re.match(r'([A-Z][a-z]?)(\d*\.?\d*)', ls)
        if match:
            ele = match.group(1)
            num = float(match.group(2))  if match.group(2) else 1.0
            com_dic[ele] = num
    s = sum(com_dic.values())
    for key in com_dic:
        com_dic[key] = round(com_dic[key]/s, 4)
    return com_dic

sta_formula_dic={}
formula_data = pd.read_csv('formula.csv')
for f in formula_data.values:
    sta_formula_dic[f[0]] = f[1]

data = pd.read_csv('materials.csv')

n = data.shape[0]
m = data.shape[1]
for i in range(n):
    com = data.values[i,0]
    com = sta_formula_dic[com]
    dic = composition(com)
    for j in range(1,m):
        if data.columns[j] in dic:
            data.iloc[i,j] = dic[data.columns[j]]
        else:
            data.iloc[i,j] = 0
# print(data)
data.to_csv('materials2.csv',index=False)
