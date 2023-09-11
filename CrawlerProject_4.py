# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 16:04:12 2023

@author: user
"""

#%% 繪製商品銷量長條圖

import pymysql
import plotly.graph_objs as go
import plotly.offline as pyo
# import plotly.express as px

# 連接資料庫  MySQL資料庫 TCP網路協定預設的主機位址為：localhost，Port為：3306 埠
db = pymysql.connect(host='localhost', port=3306, user='root', password='yeeeeeee', db='webcrawler_project', charset='utf8')
print ("資料庫連接ok")

# 建立存取游標
cursor = db.cursor()

# SQL語句
# 在游標處建立一個資料表  execute -> 執行SQL語法

# 商品總銷量數據統計
sql1 = "SELECT SALES, COUNT(*) Amount FROM webcrawler_project.mouseproducts GROUP BY SALES ORDER BY Amount DESC"

cursor.execute(sql1)
sales_amount = cursor.fetchall()

sales_list = ['總銷量 < 50', '總銷量 > 50', '總銷量 > 100', '總銷量 > 500',
              '總銷量 > 1000', '總銷量 > 3000', '總銷量 > 5000', '總銷量 > 8000',
              '總銷量 > 1萬', '總銷量 > 1.5萬', '總銷量 > 3萬', '總銷量 > 5萬',
              '總銷量 > 10萬', '總銷量 > 15萬', '總銷量 > 20萬']

amount_list = [497, 112, 222, 44, 43, 26, 6, 8, 3, 9, 4, 4, 2, 2, 1]
# print(sum(amount_list))

trace = go.Bar(x = sales_list, y = amount_list, text = amount_list)
layout = go.Layout(title_text = '商品總銷量數據統計', font_size=15)
fig = go.Figure(data=trace, layout=layout)

pyo.plot(fig, filename='sales_amount.html')

db.close()  # 關閉連接資料庫

#%% 繪製商品類型數量長條圖

import pymysql
import plotly.graph_objs as go
import plotly.offline as pyo

# 連接資料庫  MySQL資料庫 TCP網路協定預設的主機位址為：localhost，Port為：3306 埠
db = pymysql.connect(host='localhost', port=3306, user='root', password='yeeeeeee', db='webcrawler_project', charset='utf8')
print ("資料庫連接ok")

# 建立存取游標
cursor = db.cursor()

# SQL語句
# 在游標處建立一個資料表  execute -> 執行SQL語法

# 商品類型數量統計

sql1 = "SELECT DISTINCT PRODUCT FROM `mouseproducts` WHERE (PRODUCT LIKE '%無線%' OR PRODUCT LIKE '%藍牙%' OR PRODUCT LIKE '%藍芽%')"
cursor.execute(sql1)
mouse_B = cursor.fetchall()
# print(len(mouse_B))

sql2 = "SELECT DISTINCT PRODUCT FROM `mouseproducts` WHERE PRODUCT LIKE '%有線%'"
cursor.execute(sql2)
mouse_L = cursor.fetchall()

sql3 = "SELECT DISTINCT PRODUCT FROM `mouseproducts` WHERE PRODUCT LIKE '%軌跡%'"
cursor.execute(sql3)
mouse_TB = cursor.fetchall()

sql4 = "SELECT DISTINCT PRODUCT FROM `mouseproducts` WHERE PRODUCT LIKE '%垂直%'"
cursor.execute(sql4)
mouse_V = cursor.fetchall()

sql5 = "SELECT DISTINCT PRODUCT FROM `mouseproducts` WHERE PRODUCT LIKE '%電競%'"
cursor.execute(sql5)
mouse_ES = cursor.fetchall()

sql6 = "SELECT DISTINCT PRODUCT FROM `mouseproducts` WHERE PRODUCT LIKE '%靜音%'"
cursor.execute(sql6)
mouse_M = cursor.fetchall()

sql7 = """SELECT DISTINCT PRODUCT FROM `mouseproducts` WHERE 
        (PRODUCT NOT LIKE '%無線%' AND PRODUCT NOT LIKE '%藍芽%' 
         AND PRODUCT NOT LIKE '%藍牙%' AND PRODUCT NOT LIKE '%有線%' 
         AND PRODUCT NOT LIKE '%軌跡%' AND PRODUCT NOT LIKE '%垂直%')"""
cursor.execute(sql7)
mouse_O = cursor.fetchall()

mouse_type = ['藍芽無線滑鼠', '有線滑鼠', '軌跡球滑鼠', '垂直滑鼠', '電競滑鼠', '靜音滑鼠', '其他未標明']
mouse_amount = [len(mouse_B), len(mouse_L), len(mouse_TB), len(mouse_V), len(mouse_ES), len(mouse_M), len(mouse_O)]

trace = go.Bar(x = mouse_type, y = mouse_amount, text = mouse_amount)
layout = go.Layout(title_text = '商品類型數量統計', font_size=15)
fig = go.Figure(data=trace, layout=layout)

pyo.plot(fig, filename='product_type.html')

db.close()  # 關閉連接資料庫
