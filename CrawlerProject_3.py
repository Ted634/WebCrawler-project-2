# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 20:27:14 2023

@author: user
"""

#%% 繪製商品銷量長條圖

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
sql = "SELECT SALES FROM mouseproducts"

try:
    cursor.execute(sql)
    print ("資料表查詢成功")
except:
    db.rollback()
    print('資料表查詢失敗')     
db.commit() # 送出執行以上SQL語法的操作

sales_data = cursor.fetchall()

# 商品種類數量前10名品牌
sql1 = "SELECT DISTINCT PRODUCT FROM mouseproducts WHERE PRODUCT LIKE %s"

# Logitech
cursor.execute(sql1, '%Logitech%')
Logitech = cursor.fetchall()

# ASUS
cursor.execute(sql1, '%ASUS%')
Asus = cursor.fetchall()

# KINYO
cursor.execute(sql1, '%KINYO%')
Kinyo = cursor.fetchall()

# Razer
cursor.execute(sql1, '%Razer%')
Razer = cursor.fetchall()

# Microsoft
cursor.execute(sql1, '%微軟%')
Microsoft = cursor.fetchall()

# E-books
cursor.execute(sql1, '%E-books%')
Ebooks = cursor.fetchall()

# DIKE
cursor.execute(sql1, '%DIKE%')
Dike = cursor.fetchall()

# ELECOM
cursor.execute(sql1, '%ELECOM%')
Elecom = cursor.fetchall()

# INTOPIC
cursor.execute(sql1, '%INTOPIC%')
Intopic = cursor.fetchall()

# FOXXRAY
cursor.execute(sql1, '%FOXXRAY%')
Foxxray = cursor.fetchall()

brand = ['Logitech', 'ASUS', 'KINYO', 'Razer', 'Microsoft', 'E-books', 'DIKE', 'ELECOM', 'INTOPIC', 'FOXXRAY']
prod_count = [len(Logitech), len(Asus), len(Kinyo), len(Razer), len(Microsoft), len(Ebooks), len(Dike), len(Elecom), len(Intopic), len(Foxxray)]

trace = go.Bar(x = brand, y = prod_count, text = prod_count)
layout = go.Layout(title_text = '商品種類數量前10名品牌')
fig = go.Figure(data=trace, layout=layout)

pyo.plot(fig, filename='top10brand.html')

db.close()  # 關閉連接資料庫

