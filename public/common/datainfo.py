#对Excel表进行读取
#coding=utf-8
import codecs
import os
import xlrd
from config import globalparam
from selenium.webdriver.support.ui import WebDriverWait

"""
data_path=globalparam.data_path
def get_xls_to_dict(xlsname,sheetname):
    '''
    读取Excel表结果为dict
    第一行为字典的key,下面的为值
    return [{'title':'1','user':'root'}]
    :param xlsname:
    :param sheetname:
    :return:
    '''
    dataresult=[]
    result=[]
    datapath=os.path.join(data_path,xlsname)
    xls1=xlrd.open_workbook(datapath)
    table=xls1.sheet_by_name(sheetname)
    for i in range(0,table.nrows):
        dataresult.append(table.row_values(i))
    #dataresult=[table.row_values(i) for i in range(0,table.nrows())]
    #将list转化成dict
    for i in range(1,len(dataresult)):
        temp=dict(zip(dataresult[0],dataresult[i]))
        result.append(temp)

    #result=[dict(zip(dataresult[0],dataresult[i])) for i in range(1,len(dataresult))]
    return result

def get_xls_to_list(excelname,sheetname):
    '''
    读取Excel表，返回一个list
    :param excelname:
    :param sheetname:
    :return:
    '''
    datapath=os.path.join(data_path,excelname)
    excel=xlrd.open_workbook(datapath)
    table=excel.sheet_by_name(sheetname)
    result=[table.row_values(i)[0].strip() for i in range(1,table.nrows)]
    return result

if __name__=="__main__":
    res=get_xls_to_list("testdata.xlsx","Sheet1")
    #res=get_xls_to_dict("testdata.xlsx","Sheet1")
    print(res)
"""

def open_excel(file="testdata.xlsx"):
    try:
        data=xlrd.open_workbook(file)   #打开Excel文件读取数据
        return data
    except Exception as e:
        print(str())

def get_xls_to_list(file="testdata.xlsx",colnameindex=0,by_index=0):
    #根据索引获取Excel表格中的数据，file：Excel文件路径， colnameindex：表头列名所在行的索引 by_index表的索引
    data=open_excel(file)
    table=data.sheets()[by_index]  #通过索引顺序获取一个工作表
    nrows=table.nrows  #获取行数
    colnames=table.row_values(colnameindex)  #获取某一行数据
    list=[]
    for rownum in range(1,nrows):
        row=table.row_values(rownum)
        if row:
            app={}
            for i in range(len(colnames)):
                app[colnames[i]]=row[i]
                list.append(app)
    return list



