import pandas as pd
import numpy as np

def normalization(data):
   _range = np.max(data) - np.min(data) 
   return (data-np.min(data))/_range

data_use = pd.read_excel('swine-data-analysis\data_clear_and_analysis\database\database_v1.0.xlsx', sheet_name="workspace")

data_price = pd.DataFrame(data_use[['日期', '市场价格（外三元猪）']])
data_price = data_price.set_index('日期')
data_price = data_price.resample('M').mean()

test = normalization(data_price['市场价格（外三元猪）'])
data_price['价格归一化'] = test

data_price['价格环比'] = data_price['市场价格（外三元猪）'].pct_change(periods=1)
data_price['归一环比'] = data_price['价格归一化'].pct_change(periods=1)

columnsList = data_use.columns.to_list()
columnsList.pop(0)

for i in range(len(columnsList)):
    if i == 0:
        data1 = pd.DataFrame(data_use[['日期', columnsList[i]]])
        data1 = pd.DataFrame(data1.set_index('日期'))
        data1 = data1.resample('M').mean()
        print('表格 %s 已创建' % (columnsList[i]))
    else:
        data2 = pd.DataFrame(data_use[['日期', columnsList[i]]])
        data2 = pd.DataFrame(data2.set_index('日期'))
        data2 = data2.resample('M').mean()
        data1 = data1.join(data2, how = 'outer')
        print('表格 %s 添加' % (columnsList[i]))

# data1['全国生猪出栏'] = data1['全国生猪出栏'].replace({0:np.NaN})
for i in range(len(columnsList)):
    data1[columnsList[i]] = data1[columnsList[i]].replace({0:np.NaN})

for i in range(len(columnsList)):
    a = columnsList[i] + str('归一化')
    data1[a] = normalization(data1[columnsList[i]])

data1.head()
data1.to_excel('normalization.xlsx')