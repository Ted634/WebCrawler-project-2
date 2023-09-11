# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 21:34:43 2023

@author: user
"""

#%% 繪製多種商品銷量與價格分布圖

import pymysql
import plotly.graph_objs as go
import plotly.offline as pyo
# import pandas as pd
# import plotly.express as px


# 連接資料庫  MySQL資料庫 TCP網路協定預設的主機位址為：localhost，Port為：3306 埠
db = pymysql.connect(host='localhost', port=3306, user='root', password='yeeeeeee', db='webcrawler_project', charset='utf8')
print ("資料庫連接ok")

# 建立存取游標
cursor = db.cursor()

# SQL語句
# 在游標處建立一個資料表  execute -> 執行SQL語法

# 多種商品銷量與價格分布統計
# 全部
sql1 = "SELECT PRICE FROM `mouseproducts` ORDER BY SALESAMOUNT"
cursor.execute(sql1)
priceData = cursor.fetchall()
# priceData_L = list(map(list, priceData)) # map() 可以將函數應用於迭代中的每個項目。與 list() 一起使用，將包含數组的數组轉換為嵌套串列
priceData_F = []
for price1 in priceData:
    for price2 in price1:
        priceData_F.append(price2)

sql2 = "SELECT SALES FROM `mouseproducts` ORDER BY SALESAMOUNT"
cursor.execute(sql2)
salesData = cursor.fetchall()
salesData_F = []
for sales1 in salesData:
    for sales2 in sales1:
        salesData_F.append(sales2)

sql3 = "SELECT PRODUCT FROM `mouseproducts` ORDER BY SALESAMOUNT"
cursor.execute(sql3)
productData = cursor.fetchall()
productData_F = []
for product1 in productData:
    for product2 in product1:
        productData_F.append(product2)

trace1 = go.Scatter(x = priceData_F, y = salesData_F, mode = 'markers',
                   text = productData_F, name = '全部')
# 無線滑鼠
sql4 = "SELECT DISTINCT PRODUCT, PRICE, SALES FROM `mouseproducts` WHERE (PRODUCT LIKE '%無線%' OR PRODUCT LIKE '%藍牙%' OR PRODUCT LIKE '%藍芽%') ORDER BY SALESAMOUNT"
cursor.execute(sql4)
mouseBData = cursor.fetchall()
priceDataB_F = []
for price1 in mouseBData:
    priceDataB_F.append(price1[1])

salesDataB_F = []
for sales1 in mouseBData:
    salesDataB_F.append(sales1[2])

productDataB_F = []
for product1 in mouseBData:
    productDataB_F.append(product1[0])

trace2 = go.Scatter(x = priceDataB_F, y = salesDataB_F, mode = 'markers',
                   text = productDataB_F, name = '無線滑鼠')
# 有線滑鼠
sql5 = "SELECT DISTINCT PRODUCT, PRICE, SALES FROM `mouseproducts` WHERE PRODUCT LIKE '%有線%' ORDER BY SALESAMOUNT"
cursor.execute(sql5)
mouseLData = cursor.fetchall()
priceDataL_F = []
for price1 in mouseLData:
    priceDataL_F.append(price1[1])

salesDataL_F = []
for sales1 in mouseLData:
    salesDataL_F.append(sales1[2])

productDataL_F = []
for product1 in mouseLData:
    productDataL_F.append(product1[0])

trace3 = go.Scatter(x = priceDataL_F, y = salesDataL_F, mode = 'markers',
                   text = productDataL_F, name = '有線滑鼠')
# 軌跡球滑鼠
sql6 = "SELECT DISTINCT PRODUCT, PRICE, SALES FROM `mouseproducts` WHERE PRODUCT LIKE '%軌跡%' ORDER BY SALESAMOUNT"
cursor.execute(sql6)
mouseTBData = cursor.fetchall()
priceDataTB_F = []
for price1 in mouseTBData:
    priceDataTB_F.append(price1[1])

salesDataTB_F = []
for sales1 in mouseTBData:
    salesDataTB_F.append(sales1[2])

productDataTB_F = []
for product1 in mouseTBData:
    productDataTB_F.append(product1[0])

trace4 = go.Scatter(x = priceDataTB_F, y = salesDataTB_F, mode = 'markers',
                   text = productDataTB_F, name = '軌跡球滑鼠')
# 垂直滑鼠
sql7 = "SELECT DISTINCT PRODUCT, PRICE, SALES FROM `mouseproducts` WHERE PRODUCT LIKE '%垂直%' ORDER BY SALESAMOUNT"
cursor.execute(sql7)
mouseVData = cursor.fetchall()
priceDataV_F = []
for price1 in mouseVData:
    priceDataV_F.append(price1[1])

salesDataV_F = []
for sales1 in mouseVData:
    salesDataV_F.append(sales1[2])

productDataV_F = []
for product1 in mouseVData:
    productDataV_F.append(product1[0])

trace5 = go.Scatter(x = priceDataV_F, y = salesDataV_F, mode = 'markers',
                   text = productDataV_F, name = '垂直滑鼠')
# 電競滑鼠
sql8 = "SELECT DISTINCT PRODUCT, PRICE, SALES FROM `mouseproducts` WHERE PRODUCT LIKE '%電競%' ORDER BY SALESAMOUNT"
cursor.execute(sql8)
mouseESData = cursor.fetchall()
priceDataES_F = []
for price1 in mouseESData:
    priceDataES_F.append(price1[1])

salesDataES_F = []
for sales1 in mouseESData:
    salesDataES_F.append(sales1[2])

productDataES_F = []
for product1 in mouseESData:
    productDataES_F.append(product1[0])

trace6 = go.Scatter(x = priceDataES_F, y = salesDataES_F, mode = 'markers',
                   text = productDataES_F, name = '電競滑鼠')
# 靜音滑鼠
sql9 = "SELECT DISTINCT PRODUCT, PRICE, SALES FROM `mouseproducts` WHERE PRODUCT LIKE '%靜音%' ORDER BY SALESAMOUNT"
cursor.execute(sql9)
mouseMData = cursor.fetchall()
priceDataM_F = []
for price1 in mouseMData:
    priceDataM_F.append(price1[1])

salesDataM_F = []
for sales1 in mouseMData:
    salesDataM_F.append(sales1[2])

productDataM_F = []
for product1 in mouseMData:
    productDataM_F.append(product1[0])

trace7 = go.Scatter(x = priceDataM_F, y = salesDataM_F, mode = 'markers',
                   text = productDataM_F, name = '靜音滑鼠')


data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7]

layout = go.Layout(title_text = '多種商品銷量與價格分布統計', font_size=15,
                   xaxis=dict(tickmode = 'auto', tickformat = '$', title = '商品價格'),
                   yaxis=dict(tickmode = 'auto', title = '商品總銷量'))
fig = go.Figure(data=data, layout=layout)

# fig.update_xaxes(title_text='商品價格')
# fig.update_yaxes(title_text='商品總銷量')

pyo.plot(fig, filename='sales_type_price.html')

db.close()  # 關閉連接資料庫