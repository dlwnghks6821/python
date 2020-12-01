import urllib.request
import urllib.parse
import sys
#python.a.py 108
if len(sys.argv)<2:
    argv="108"
else:
    argv=sys.argv[1]

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values={'stnId':argv}
params=urllib.parse.urlencode(values)
url = API+"?"+params #Get method
print(url)
data=urllib.request.urlopen(url).read()
text=data.decode('utf-8')
print(text)


'''
url = "http://api.aoikujira.com/ip/ini"
savename="c:/img/test.png"
#urllib.request.urlretrieve(url,savename)
mem = urllib.request.urlopen(url).read()
text=mem.decode('utf-8')
print(text)

with open(savename,mode='wb') as f:
    f.write(mem)
    print("저장되었습니다.")
'''
