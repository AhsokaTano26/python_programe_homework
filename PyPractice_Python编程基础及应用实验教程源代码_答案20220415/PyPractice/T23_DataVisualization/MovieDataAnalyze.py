import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator

datas = pd.read_csv(r'2015-2020.txt', index_col=0)
datas = datas.sort_index(ascending=False)
datas = pd.DataFrame(datas.values, index=range(1, 11), \
    columns=datas.columns)
data2020 = pd.read_csv(r'2020.txt')


def drawLines():
    ax = plt.subplot(131)
    for date in datas.columns:
        plt.plot([10 - i for i in range(datas.shape[0])], \
            datas[date], label=date)
    plt.ylim(0, 600000)
    ymajorLocator = MultipleLocator(50000)
    xmajorLocator = MultipleLocator(1)
    ax.yaxis.set_major_locator(ymajorLocator)
    ax.xaxis.set_major_locator(xmajorLocator)
    plt.title('2015-2020年度票房Top10折线图')
    plt.xlabel('票房名次')
    plt.grid()
    plt.legend()


def drawBar():
    plt.subplot(132)
    labels = range(2015, 2021)
    i = 0
    x = np.arange(len(datas.columns))
    for index in datas.index:
        plt.bar(x + i * 0.1, datas.loc[index], width=0.1, \
            tick_label=labels)
        i += 1
    plt.title('2015-2020年度票房Top10柱状图')
    plt.xlabel('票房年度')
    plt.grid()


def drawPie():
    plt.subplot(233)
    plt.pie(datas['2019'], autopct='%1.1f%%')
    plt.title('2019年度票房Top10饼图')
    plt.subplot(236)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['font.family'] = 'sans-serif'
    plt.pie(data2020['boxoffice'], autopct='%1.1f%%', \
        labels=data2020['name'])
    plt.title('2020年度票房Top10饼图')


if __name__ == '__main__':
    plt.subplots(figsize=(20, 8))
    drawLines()
    drawBar()
    drawPie()
    plt.show()
