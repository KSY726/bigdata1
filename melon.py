import requests
from bs4 import BeautifulSoup

# 웹에 접속
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}
r = requests.get("https://www.melon.com/",headers=header)
print(r) # 접속이 잘됐는지 확인

# html 정보 가지고오기
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup) # 가져온 html 데이터 출력

# #conts > div.chart > div > ul > li.on.nth1 > div > ul > li:nth-child(1) > div.rank_cntt > div.rank_info > p > a
for i in range(1,11):
    title = soup.select_one(f'#conts > div.chart > div > ul > li.on.nth1 > div > ul > li:nth-child({i}) > div.rank_cntt > div.rank_info > p > a')
    print(f'{i}위 {title.text}')