# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 19:52:08 2023

@author: user
"""

#%% 爬取momo購物網 "滑鼠" 的銷售資訊

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.momoshop.com.tw/main/Main.jsp'
# url = 'https://www.momoshop.com.tw/search/searchShop.jsp?keyword=%E6%BB%91%E9%BC%A0&searchType=1&cateLevel=0&cateCode=&curPage=1&_isFuzzy=0&showType=chessboardType&serviceCode=MT01'
driver = webdriver.Chrome()
driver.get(url)

sleep(1)

elem = driver.find_element(By.NAME, "keyword")
elem.clear()
elem.send_keys('滑鼠')
elem.send_keys(Keys.RETURN)

sleep(1)

products_list, price_list, sales_list = [], [], []
soup = BeautifulSoup(driver.page_source, 'lxml')
i = 1

page = 1
print('MOMO商品 page', page)
print('-------------------------------------------------')

products = soup.find_all('h3', attrs={'class':'prdName'})
for product in products:
    # print(product.text)
    products_list.append(product.text)

prices = soup.find_all('span', attrs={'class':'price'})
for price in prices:
    # print(price.text)
    price_list.append(price.text.replace('$', '').replace(',', ''))

sales = soup.find_all('span', attrs={'class':'totalSales goodsTotalSales'})
for sale in sales:
    # print(sale.text)
    sales_list.append(sale.text)

print('MOMO商品 page', page,'讀取完畢，準備下一頁')
print('-------------------------------------------------')

try:
    nextpage = driver.find_element(By.LINK_TEXT, '下一頁').click()
except:
    print('已經是最後一頁')

for page in range(2, 34):
    # url = 'https://www.momoshop.com.tw/search/searchShop.jsp?keyword=%E6%BB%91%E9%BC%A0&searchType=1&cateLevel=0&cateCode=&curPage=' + str(page) + '&_isFuzzy=0&showType=chessboardType&serviceCode=MT01'
    # driver = webdriver.Chrome()
    # driver.get(url)
    
    sleep(2)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    print('MOMO商品 page', page)
    print('-------------------------------------------------')

    products = soup.find_all('h3', attrs={'class':'prdName'})
    for product in products:
        # print(product.text)
        products_list.append(product.text)

    prices = soup.find_all('span', attrs={'class':'price'})
    for price in prices:
        # print(price.text)
        price_list.append(price.text.replace('$', '').replace(',', ''))

    sales = soup.find_all('span', attrs={'class':'totalSales goodsTotalSales'})
    for sale in sales:
        # print(sale.text)
        sales_list.append(sale.text)

    print('MOMO商品 page', page,'讀取完畢，準備下一頁')
    print('-------------------------------------------------')
    sleep(8)
    try:
        nextpage = driver.find_element(By.LINK_TEXT, '下一頁').click()
    except:
        print('已經是最後一頁')

title_list = ['Product', 'Price', 'Sales']
final_text = [products_list, price_list, sales_list]

data = {}
for title, text in zip(title_list, final_text):
    data[title] = text

data_df = pd.DataFrame(data)

data_df.to_csv("ProductsInfo.csv", encoding='utf-8', index=False, header=True)

driver.quit()
