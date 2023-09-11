# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 22:20:14 2023

@author: user
"""

#%% 建立資料表

import pymysql

# 連接資料庫  MySQL資料庫 TCP網路協定預設的主機位址為：localhost，Port為：3306 埠
db = pymysql.connect(host='localhost', port=3306, user='root', password='yeeeeeee', db='webcrawler_project', charset='utf8')
print ("資料庫連接ok")

# 建立存取游標
cursor = db.cursor()

# SQL語句
# 在游標處建立一個資料表  execute -> 執行SQL語法
try:
    cursor.execute('''
        CREATE TABLE MouseProducts
       (SN INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
       PRODUCT TEXT NOT NULL,
       PRICE INT NOT NULL,
       SALES TEXT,
       SALESAMOUNT INT);
       ''')

    print ("資料表建立成功")
except:
    db.rollback()
    print('資料表建立失敗')
        
db.commit() # 送出執行以上SQL語法的操作
db.close()  # 關閉連接資料庫

#%% 將CSV檔案中的資料寫入資料庫中

import pandas as pd
import pymysql

df = pd.read_csv('ProductsInfo.csv', encoding='utf-8')
df.info()

# print(df['Product'])
products = list(df['Product'])

# print(df['Price'])
prices = list(df['Price'])

# print(df['Sales'])
sales = list(df['Sales'])

# 連接資料庫  MySQL資料庫 TCP網路協定預設的主機位址為：localhost，Port為：3306 埠
db = pymysql.connect(host='localhost', port=3306, user='root', password='yeeeeeee', db='webcrawler_project', charset='utf8')
print ("資料庫連接ok")

# 建立存取游標
cursor = db.cursor()

# SQL語句
# 在游標處建立一個資料表  execute -> 執行SQL語法

for pro, pri, sal in zip(products, prices, sales):
    # print(pro, pri, sal)
    sql1 = "insert into mouseproducts(PRODUCT,PRICE,SALES) values(%s,%s,%s)"
    try:
        cursor.execute(sql1, (str(pro),int(pri),str(sal)))
        print ("資料表建立成功")
    except:
        db.rollback()
        print('資料表建立失敗')
        
    db.commit() # 送出執行以上SQL語法的操作
db.close()  # 關閉連接資料庫


