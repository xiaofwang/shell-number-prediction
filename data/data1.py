import pandas as pd

raw_data = pd.read_csv('data.csv')

sta_formula_dic={}
formula_data = pd.read_csv('formula.csv')
for f in formula_data.values:
    sta_formula_dic[f[0]] = f[1]

data = raw_data[raw_data['材料'].isin(sta_formula_dic)]

data.to_csv('data.csv', index=False)

