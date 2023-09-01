from wxauto import WeChat
import re
import numpy as np
import pandas as pd
import datetime
import pymysql

# 早间投票
def getTmrAndDOTmrMean(condition1, condition2):
    # 打开文件传输助手并获取信息
    wx = WeChat()
    wx.ChatWith('文件传输助手')
    msgs = wx.GetAllMessage
    # 获取信息长度
    len(msgs)
    # 判断信息时间
    tmrList = []
    for x in range(len(msgs)-1):
        if msgs[x][1].startswith(condition1):
            useTimeIndex = x + 1
            for y in range(useTimeIndex, len(msgs)-1):
                if msgs[y][1].startswith(condition2):
                    i = y + 1
                    for i in range(i, len(msgs)-1):
                        dataUse_tmr = re.findall(r"\d", msgs[i][1])
                        if len(dataUse_tmr) == 2:
                            for x in dataUse_tmr:
                                tmrList.append(int(x))
                                print('已加入%s'%(int(x)))
                        else:
                            tmrList.append(int(dataUse_tmr[0]))
                            print('已加入%s'%(int(dataUse_tmr[0])))
                        dataUse_DOtmr = re.findall('[a-zA-Z]', msgs[i][1])
                        if len(dataUse_DOtmr) == 0:
                            continue
    # 计算各个投票次数
    number1 = tmrList.count(1)     
    number2 = tmrList.count(2)
    number3 = tmrList.count(3)
    number4 = tmrList.count(4)
    number5 = tmrList.count(5)
    number_total = [number1, number2, number3, number4, number5]  
    number_sum = sum(number_total)
    number_use1 = number1/number_sum
    number_use2 = number2/number_sum
    number_use3 = number3/number_sum
    number_use4 = number4/number_sum
    number_use5 = number5/number_sum
    return(
        number_use1,number_use2,number_use3,number_use4,number_use5,
    )

def writeDB(result):
    # 打开数据库连接
    conn = pymysql.connect(host='gz-cdb-50zykywd.sql.tencentcdb.com',
                        port=58639,
                        user='user_biz',
                        password='V6VK2MtXYQCY',
                        database='biz_data')
    
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()
    today = datetime.date.today()
    today = today.strftime("%Y/%m/%d")

    # 使用 execute()  方法执行 SQL 查询 
    cursor.execute(
        "INSERT INTO gp_expectation_copy VALUES ('%s', %.4f, %.4f, %.4f, %.4f, %.4f);"
        % (today, result[0], result[1], result[2], result[3], result[4] , result[5])
    )
    conn.commit()

    cursor.close()
    conn.close()

if __name__ == '__main__':
    useTime = str(input("请输入查询时间:"))
    useCondition = str(input('请输入查询条件：'))
    print('开始查询')
    result = getTmrAndDOTmrMean(useTime, useCondition)
    
    writeDB(result)