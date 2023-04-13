'''
将收储和放储政策做成dummy值添加到猪价表中，后收集对猪价的影响来分析影响时长并做总结。
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 使用日度猪价

dataPigPrice = pd.read_excel(r"D:\git\新建文件夹\swine-data-analysis\data_clear_and_analysis\database\GL_20230227.xlsx", sheet_name="出栏价格")

dataPigPrice = dataPigPrice.iloc[:, 1:3]
dataPigPrice = dataPigPrice.drop(index = dataPigPrice.index[[0,1]])
dataPigPrice.columns = ['Time', 'PigPrice']

# 创建空列放置政策dummy

dataPigPrice['收储'] = ''

dataPigPrice.head()

plt.plot(dataPigPrice['Time'], dataPigPrice['PigPrice'])
plt.show()

dataUse = pd.DataFrame(dataPigPrice).set_index('Time')
dataUse_year = dataUse['2021':'2022'] 

# 收储引入
dataSC = pd.read_excel(r"D:\git\新建文件夹\swine-data-analysis\data_clear_and_analysis\database\GL_20230227.xlsx", sheet_name='收储')
dataSC = dataSC.iloc[2:, 1:]
dataSC = dataSC.drop('Unnamed: 2', axis =1)
dataSC = dataSC.drop('Unnamed: 4', axis = 1)
dataSC.columns = ['Time', '实际收储']

dataSC

dataSC = pd.DataFrame(dataSC.set_index('Time'))

index = dataSC[dataSC['实际收储']==1500].index.to_list()[0]
str(index)

dataCombined1 = dataUse_year
dataCombined1['实际收储'] = ''
dataCombined1['实际收储量'] = ''
indexList = []
for i in dataSC['实际收储']:
    if i > 0:
        index = dataSC[dataSC['实际收储']==i].index.to_list()[0]
        dataCombined1['实际收储'].loc[str(index)] = 1
        
for i in dataSC['实际收储']:
    if i > 0:
        index = dataSC[dataSC['实际收储']==i].index.to_list()[0]
        dataCombined1['实际收储量'].loc[str(index)] = i
dataCombined1 = dataCombined1.drop('收储', axis=1)

dataCombined1['PigPrice'].fillna(method="bfill", inplace=True)
dataCombined1
dataCombined1.to_excel('demo.xlsx')