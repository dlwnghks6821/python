from bs4 import BeautifulSoup #html �м� ���̺귯��.
import urllib.request as r
#ȯ���� ���̹� ȯ������ �����ͺ���

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