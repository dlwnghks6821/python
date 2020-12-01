from bs4 import BeautifulSoup #html 분석 라이브러리.
import urllib.request as r
#환율을 네이버 환율에서 가져와보자

url ='http://finance.naver.com/marketindex'
res = r.urlopen(url)
soup=BeautifulSoup(res,'html.parser')
price = soup.select_one('a.usd div.head_info > span.value').string
print("USD/KRW["+price+"]")
price = soup.select_one('a.jpy div.head_info > span.value').string
print('JPY/KRW['+price+']')
price = soup.select_one('a.eur div.head_info > span.value').string
print('EUR/KRW['+price+']')
price = soup.select_one('a.cny div.head_info > span.value').string
print('CNY/KRW['+price+']')