import pandas as pd
import numpy as np

data = pd.read_excel(r'D:\git\新建文件夹\swine-data-analysis\data_clear_and_analysis\database\Clear_v1.0.xlsm', sheet_name='workspace')



dataUse = data.resample('M', on='日期').mean()

dataUse.head(20)