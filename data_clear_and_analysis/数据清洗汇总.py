import pandas as pd
import numpy as np

data = pd.read_excel(r'D:\git\新建文件夹\swine-data-analysis\data_clear_and_analysis\database\Clear_v1.0.xlsm', sheet_name='workspace')

columnsList = data.columns.to_list()
columnsList.drop('日期')

dataNF = pd.DataFrame(data[['日期', '能繁存栏（国家统计局）']])
dataNF = pd.DataFrame(dataNF.set_index('日期'))
dataNF = dataNF.resample('M').mean()

dataZJ = pd.DataFrame(data[['日期', '猪价']])
dataZJ = pd.DataFrame(dataZJ.set_index('日期'))
dataZJ = dataZJ.resample('M').mean()

data1 = dataZJ.join(dataNF, how='outer')
