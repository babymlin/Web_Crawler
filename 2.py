# -*- coding: utf-8 -*-
"""
Created on Fri May  7 15:55:08 2021

@author: user
"""

#0510作業1
#101_AI_林建名

import requests
import os
from prettytable import PrettyTable

def main(item, page="1", sort="sale/dc"):
    os.system('cls' if os.name == 'nt' else 'clear')
    url = "https://ecshweb.pchome.com.tw/search/v3.3/all/results"
    headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    }
    params = {
        "q": item,
        "page": page,
        "sort": sort
        }
    respons = requests.get(url=url, headers=headers, params=params)
    
    code = respons.status_code
    if code == 400:
        print("頁碼超過範圍！")
    elif code != 200:
        print(f"讀取不到頁面，返回代碼： {code}")
        
    datas = respons.json()["prods"]
    table = PrettyTable(["名稱", "價格"], encoding='utf8')
    table.align = 'l'
    for val in datas:
        table.add_row([val["name"], val["price"]])
    print(table)
    
inp = input("關鍵字:")
main(inp)
while True:
    inppage = input("前往頁碼：")
    if inppage == "0":
        print("頁碼超過範圍！")
        break
    elif inppage.isdigit() == False :
        print("輸入的不是數字！")
        break
    else:
        try:
            main(item=inp, page=inppage)
        except:
            break