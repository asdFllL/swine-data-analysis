# 通过格兰杰因果验证去测试毛白价差、白条价格对猪价是否在数据上有因果关系
from statsmodels.tsa.stattools import grangercausalitytests
from statsmodels.tsa.api import VAR

