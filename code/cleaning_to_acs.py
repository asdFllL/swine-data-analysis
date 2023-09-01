import openpyxl
import pyodbc

'''打开金猪数据并读取地区标肥价格'''
data_path = r"D:\Chen_Keyu\database\金猪-20230727.xlsx"
wb = openpyxl.load_workbook(data_path)
ws = wb.get_sheet_by_name('Sheet1')
