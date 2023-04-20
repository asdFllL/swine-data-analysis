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
