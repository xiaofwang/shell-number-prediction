import pandas as pd
import numpy as np

def norm(d):
    mu = np.mean(d)
    sigma = np.std(d)
    d_norm = (d - mu) / sigma
    return d_norm

# 读取数据文件，除去不在标准化公式中的列
raw_data = pd.read_csv('data.csv')
sta_formula_dic={}
formula_data = pd.read_csv('materials.csv')
n_ele = formula_data.shape[1]-1
for f in formula_data.values:
    sta_formula_dic[f[0]] = np.array(f[1:])
data = raw_data[raw_data['material'].isin(sta_formula_dic)]
n_data = data.shape[0]

# 材料矩阵
materials = np.zeros([n_data, n_ele])
materials_columns = formula_data.columns[1:]
for i in range(n_data):
    materials[i] = sta_formula_dic[data['material'][i]]
df1 = pd.DataFrame(data=materials, columns=materials_columns)
df1 = df1.loc[:, (df1 != 0).any(axis=0)]

"""materials = np.zeros(n_data)
for i in range(n_data):
    materials[i] = 0
    formula_array = sta_formula_dic[data['material'][i]]
    for j in range(n_ele):
        materials[i] += formula_array[j]*(j+1)
materials = norm(materials)
df1 = pd.DataFrame(data=materials, columns=['material'])"""

# 碳球描述符：半径，预处理
cms = []
for c in data['cms']:
    if c == 1:
        cms.append(0)
    else:
        cms.append(1)
treatment = np.zeros([n_data,2],dtype=int)
treatment[:,0] = data['alkali']
treatment[:,1] = data['acid']
print(type(treatment[0,0]))
treatment_columns = ['alkali', 'acid']
df2 = pd.DataFrame(data=treatment, columns=treatment_columns)

# 吸附描述符：浓度、溶剂、时间、温度、重复次数
concentration = data['concentration']
solvent = np.zeros([n_data,4])
solvent_columns = ['water', 'ethanol', 'glycol', 'acetone']
solvent[:,0] = data['water']
solvent[:,1] = data['ethanol']
solvent[:,2] = data['glycol']
solvent[:,3] = data['acetone']
df3 = pd.DataFrame(data=solvent, columns=solvent_columns)
time = data['time']
adsorption_tem = data['t']
repeat_n = data['repeat'].astype(int)
adsorption = concentration * adsorption_tem * time * repeat_n

# 退火描述符：升温速率、反应速率、保温时间
heating_rate1 = data['heating rate1']
reaction_rate1 = data['reaction rate1']
annealing_time1 = data['annealing time1']
heat1 = heating_rate1 * reaction_rate1 * annealing_time1
heating_rate2 = data['heating rate2']
reaction_rate2 = data['reaction rate2']
annealing_time2 = data['annealing time2']
heat2 = heating_rate2 * reaction_rate2 * annealing_time2
# 壳层数
shell_number = data['shell number'].astype(int)
print(shell_number)
# 数据预处理，吸附温度和反应速率归一化
adsorption_tem = norm(adsorption_tem)
reaction_rate1 = norm(reaction_rate1)
non_zero_values = reaction_rate2[reaction_rate2 != 0]
normalized_values = norm(non_zero_values)
reaction_rate2.loc[reaction_rate2 != 0] = normalized_values
adsorption = norm(adsorption)
heat1 = norm(heat1)
heat2 = norm(heat2)

df4 = pd.DataFrame({
    'cms':cms,
    'adsorption':adsorption,
    'heat1':heat1,
    'heat2':heat2,
    'shell_number':shell_number
})

descriptor = pd.concat([df1, df2, df3, df4], axis=1)
descriptor = descriptor[~descriptor['shell_number'].isin([0,5,6,7])]
descriptor_cleaned = descriptor.dropna(how='any')
descriptor_cleaned.to_csv('descriptor.csv', index=False)


