import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def plt_pearsonr(df):
    correlation_matrix = df.corr()
    print(correlation_matrix.shape)
    plt.figure()  # 设置图形大小
    sns.heatmap(correlation_matrix, annot=False, cmap='coolwarm', center=0)
    plt.title('Pearson Correlation Coefficient Matrix')
    plt.show()



