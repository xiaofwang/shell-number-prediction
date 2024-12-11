import pandas as pd
import numpy as np

raw_data = pd.read_csv('data.csv')

sta_formula_dic={}
formula_data = pd.read_csv('materials2.csv')
for f in formula_data.values:
    sta_formula_dic[f[0]] = np.array(f[1:])
data = raw_data[raw_data['材料'].isin(sta_formula_dic)]
print()



