# -*- coding: utf-8 -*-
"""
Created on Fri May  7 14:14:54 2021

@author: user
"""

#0507作業2
#101_AI_林建名

import requests
import warnings
warnings.filterwarnings("ignore")


url = "http://teaching.bo-yuan.net/test/requests/"

respons = requests.get(url, params={"action":" "})
respons.encoding = "utf8"
print(respons.text)

respons = requests.delete(url, params={"action":" "}, data={"id":" "})
respons.encoding = "utf8"
print(respons.text)

respons = requests.put(url, params={"action":" "}, data={"id":" ", "name":" "})
respons.encoding = "utf8"
print(respons.text)

respons = requests.patch(url, params={"action":" "}, data={"id":" ", "name":" ", "address":" "})
respons.encoding = "utf8"
print(respons.text)

respons = requests.post(url, params={"action":" "}, data={"id":" ", "name":" ", "address":" "})
respons.encoding = "utf8"
print(respons.text)