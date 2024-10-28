import requests
from bs4 import BeautifulSoup
import pandas as pd

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}
r = requests.get("https://www.melon.com/chart/index.htm",headers=header)
print(r) 

soup = BeautifulSoup(r.text, 'html.parser')

rank = [] 
for i in range(1, 101):
    rank.append(i)
print(rank)

tlist = []
title = soup.select('div.ellipsis.rank01 > span > a')
for t in title:
    tlist.append(t.text)

alist = []
artist = soup.select('div.ellipsis.rank02 > span > a:nth-child(1)')
for a in artist:
    alist.append(a.text)

df3 = pd.DataFrame({'순위': rank,
                    '제목': tlist,
                    '가수': alist})

df3.to_csv('melon100.csv', index=False)

