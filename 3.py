# -*- coding: utf-8 -*-
"""
Created on Fri May  7 20:51:10 2021

@author: babymlin
"""
#0510作業2
#101_AI_林建名

import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import warnings
warnings.filterwarnings("ignore")

url = "https://www.cwb.gov.tw/V8/C/W/TemperatureTop/County_TMax_T.html"
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    }
# params = {
#     "ID":"Fri May 07 2021 22:48:41 GMT 0800"
#     }
respons = requests.get(url, headers=headers)
code = respons.status_code
if code == 200:
    soup = BeautifulSoup(respons.text)
    countrys = soup.find_all("th", scope="row")
    temps = soup.find_all("span", class_="tem-C")
    table = PrettyTable(["地區", "氣溫"], encoding="utf8")
    table.align = "l"
    for country, temp in zip(countrys, temps):
        table.add_row([country.text, temp.text])
    print(table)
else:
    print(f"讀取不到頁面，返回代碼： {code}")