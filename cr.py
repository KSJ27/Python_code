# beautifulsoup html 소스를 Python으로 객체 변경


import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/"
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html,'html.parser')

titleList = soup.select(".lnk_hdline_article")
# class는 .  id는 #
print(titleList)


for title in titleList:
    print(title.text)

