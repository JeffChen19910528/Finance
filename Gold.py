#台灣銀行黃金價格
import time
import urllib.request as request
from bs4 import BeautifulSoup as sp
import requests

local_time = time.ctime(time.time())
url="https://rate.bot.com.tw/gold?Lang=zh-TW" ###
with request.urlopen(url) as response:
  data=response.read().decode("utf-8")
  root=sp(data,"html.parser")
  gold_in=(root.find_all("td")[5].text.replace("回售","").strip()) ###
  gold_out=(root.find_all("td")[2].text.replace("買進","").strip()) ###
  s1=("\nGold"+"\n銀行買進: "+gold_in+"\n銀行賣出: "+gold_out) ###
  note=local_time+s1
  print(s1)
  
  
# 黃金金價買價  加入每一秒自動爬蟲一次
import time
import urllib.request as request
from bs4 import BeautifulSoup as sp
import requests

local_time = time.ctime(time.time())

j=0
while j==0:
	url="https://rate.bot.com.tw/gold?Lang=zh-TW" ###
	with request.urlopen(url) as response:
	  data=response.read().decode("utf-8")
	root=sp(data,"html.parser")
	gold_in=(root.find_all("td")[5].text.replace("回售","").strip()) ###
	gold_out=(root.find_all("td")[2].text.replace("買進","").strip()) ###
	s1=("\nGold"+"\n銀行買進: "+gold_in+"\n銀行賣出: "+gold_out) ###
	note=local_time+s1
	print(s1)
	time.sleep(1)