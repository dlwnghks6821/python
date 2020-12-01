

from bs4 import BeautifulSoup #html 분석 라이브러리.

html="""
<html><body>
<ul>
<li><a href="http://www.naver.com">naver</a></li>
<li><a href="http://www.daum.net">naver</a></li>
<li><a href="http://www.google.com">naver</a></li>
</ul>
</body></html>

"""
soup = BeautifulSoup(html,"html.parser")
links=soup.find_all("a")
for a in links:
    href=a.attrs["href"]
    text=a.string
    print(text,">",href)
#print("body["+body.string+"]")