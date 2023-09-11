# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 21:46:20 2023

@author: user
"""

#%% 繪製商品銷量與價格分布圖

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

# 商品銷量與價格分布統計
# sql1 = "SELECT PRICE FROM `mouseproducts` WHERE SALES = '總銷量<50'"
sql1 = "SELECT PRICE FROM `mouseproducts` ORDER BY SALESAMOUNT"
cursor.execute(sql1)
priceData = cursor.fetchall()
priceData_L = list(map(list, priceData)) # map() 可以將函數應用於迭代中的每個項目。與 list() 一起使用，將包含數组的數组轉換為嵌套串列
priceData_F = []
for price in priceData_L:
    priceData_F.append(price[0])

# for price1 in priceData_L:
#     for price2 in price1:
#         priceData_F.append(price2)

# priceM = ['$' + str(m) for m in priceData_F]


sql2 = "SELECT SALES FROM `mouseproducts` ORDER BY SALESAMOUNT"
cursor.execute(sql2)
salesData = cursor.fetchall()
salesData_L = list(map(list, salesData))
salesData_F = []
for sales in salesData_L:
    salesData_F.append(sales[0])

sql3 = "SELECT PRODUCT FROM `mouseproducts` ORDER BY SALESAMOUNT"
cursor.execute(sql3)
productData = cursor.fetchall()
productData_L = list(map(list, productData))
productData_F = []
for product in productData_L:
    productData_F.append(product[0])

trace = go.Scatter(x = priceData_F, y = salesData_F, mode = 'markers',
                   text = productData_F, marker_color = priceData_F,
                   marker_size = 8)
layout = go.Layout(title_text = '商品銷量與價格分布統計', font_size=15,
                   xaxis=dict(tickmode = 'auto', tickformat = '$', title = '商品價格'),
                   yaxis=dict(tickmode = 'auto', title = '商品總銷量'),
                   plot_bgcolor='#abb4b9')
fig = go.Figure(data=trace, layout=layout)

# fig.update_xaxes(title_text='商品價格')
# fig.update_yaxes(title_text='商品總銷量')

pyo.plot(fig, filename='sales_price.html')

db.close()  # 關閉連接資料庫