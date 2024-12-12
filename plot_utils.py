import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def plot_pearsonr(df):
    """
    绘制描述符之间的皮尔逊相关系数热图

    参数:
    df (pd.DataFrame): 包含所有描述符的DataFrame
    """
    correlation_matrix = df.corr()
    plt.figure()  # 设置图形大小
    sns.heatmap(correlation_matrix, annot=False, cmap='coolwarm', center=0)
    plt.title('Pearson Correlation Coefficient Matrix')
    # plt.show()


def plot_model_metrics(metrics_df, metrics_to_plot):
    """
    绘制不同模型的性能指标柱状图。

    参数:
    metrics_df (pd.DataFrame): 包含模型名称和性能指标的DataFrame。
    metrics_to_plot (list of str): 要绘制的性能指标名称列表。
    """
    plt.figure(figsize=(10, 6))
    plt.title('Model Performance', fontsize=16)
    bar_width = 0.2
    index = np.arange(len(metrics_df['model']))
    for i, metric in enumerate(metrics_to_plot):
        plt.bar(index + i * bar_width, metrics_df[metric], bar_width, label=metric)
    plt.xlabel('Model')
    plt.ylabel('Score')
    plt.xticks(index + bar_width * len(metrics_to_plot) / 2 - bar_width / 2, metrics_df['model'])
    plt.legend()

    # 显示图表（通常这个函数内部不调用plt.show()，而是在调用此函数的脚本中调用）
    # plt.show()  # 注释掉这一行，以便在其他脚本中控制何时显示图表

    # 返回图表对象（可选，如果你需要在其他函数中进一步处理图表）
    # return plt.gcf()  # get current figure

