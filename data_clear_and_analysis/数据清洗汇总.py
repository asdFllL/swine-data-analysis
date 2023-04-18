#-*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_excel(r'D:\git\新建文件夹\swine-data-analysis\data_clear_and_analysis\database\Clear_v1.0.xlsm', sheet_name='workspace')

columnsList = data.columns.to_list()
columnsList.pop(0)

for i in range(len(columnsList)):
    if i == 0:
        data1 = pd.DataFrame(data[['日期', columnsList[i]]])
        data1 = pd.DataFrame(data1.set_index('日期'))
        data1 = data1.resample('M').mean()
        print('表格 %s 已创建' % (columnsList[i]))
    else:
        data2 = pd.DataFrame(data[['日期', columnsList[i]]])
        data2 = pd.DataFrame(data2.set_index('日期'))
        data2 = data2.resample('M').mean()
        data1 = data1.join(data2, how = 'outer')
        print('表格 %s 添加' % (columnsList[i]))
        
dataUse = data1['2018':'2022']

dataUse = dataUse[['猪价', '能繁存栏（国家统计局）', '农村农业部屠宰量', '历史生猪出栏']]

fig, ax1 = plt.subplots(figsize = (26,9))
ax2 = ax1.twinx()
ax3 = ax1.twinx()
ax4 = ax1.twinx()

ax3.spines['right'].set_position(('outward', 45))
ax4.spines['right'].set_position(('outward', 90))

index = dataUse.index.to_list()
img1, = ax1.plot(index, dataUse['猪价'], c = 'tab:blue')
img2, = ax2.plot(index, dataUse['能繁存栏（国家统计局）'], c = 'tab:orange')
img3, = ax3.plot(index, dataUse['农村农业部屠宰量'], c = 'tab:green')
img4, = ax4.plot(index, dataUse['历史生猪出栏'], c = 'tab:red')

axs = [ax1, ax2, ax3, ax4]
imgs = [img1, img2, img3, img4]

for i in range(len(axs)):
    axs[i].spines['right'].set_color(imgs[i].get_color())
    axs[i].set_ylabel('y{}'.format(i+1), c = imgs[i].get_color())
    axs[i].tick_params(axis='y', color = imgs[i].get_color(), labelcolor = imgs[i].get_color())
    axs[i].spines['left'].set_color(img1.get_color())

ax1.set_xlabel('Time')
ax1.set_ylabel('猪价')
ax2.set_ylabel('能繁')
ax3.set_ylabel('屠宰')
ax4.set_ylabel('出栏')

ax1.set_ylim(min(dataUse['猪价']), max(dataUse['猪价']))
ax2.set_ylim(min(dataUse['能繁存栏（国家统计局）']), max(dataUse['能繁存栏（国家统计局）']))
ax3.set_ylim(min(dataUse['农村农业部屠宰量']), max(dataUse['农村农业部屠宰量']))
ax4.set_ylim(min(dataUse['历史生猪出栏']), max(dataUse['历史生猪出栏']))

# plt.tight_layout()
# plt.savefig('猪价供需.png', dpi = 1000)
plt.grid()
plt.show()

# 需要优化x坐标显示月份，线上标记最高点最低点