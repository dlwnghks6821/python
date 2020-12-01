from bs4 import BeautifulSoup #html 분석 라이브러리.

html="""
<html><body>
<div id="meigen">
<h1>Book</h1>
<ul class="items">   
<li>unity</li>
<li>swift</li>
<li>webdesign</li>
</ul>
</div>
</body>
</html>
'''
"""
soup = BeautifulSoup(html,'html.parser')
h1 = soup.select_one("div#meigen > h1").string
print("h1="+h1)
li_list=soup.select('div#meigen > ul.items > li')
for li in li_list:
    print("li["+li.string+"]")
"""
import urllib.request as req

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
res=req.urlopen(url)
soup=BeautifulSoup(res,"html.parser")
title = soup.find("title").string
wf=soup.find('wf').string
print(title)
print(wf)

'''
"""