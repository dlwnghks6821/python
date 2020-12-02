from bs4 import BeautifulSoup
from urllib.request import *
from urllib.parse import *
from os import makedirs
import os.path, time, re

proc_files = {}


# HTML 내부에 있는 링크를 추출하는 함수

def enum_links(html, base): 
    soup =BeautifulSoup(html, "html.parser")
    links = soup.select("link[rel='stylesheet']") # CSS
    links += soup.select("a[href]")
    result = []
    
    for a in links:
        href = a.attrs['href']
        url = urljoin(base, href)
        result.append(url)
    return result

def download_file(url):
    o = urlparse(url)
    savepath = "./" + o.netloc + o.path
    if re.search(r"/$", savepath):
        savepath += "index.html"
    savedir = os.path.dirname(savepath)
    if os.path.exists(savepath): return savepath
    # 다운받을 폴더 생성
    if not os.path.exists(savedir):
        print("mkdir=", savedir)
        makedirs(savedir) 
    # 파일 다운받기
    try:
        print("download=", url)
        urlretrieve(url, savepath)
        time.sleep(1) # 11 4 (7)
        return savepath 
    except:
        print("다운실패:", url)
        return None

# HTML을 분석하고 다운받는 함수 
def analyze_html(url, root_url):
    savepath = download_file(url)
    if savepath is None: return
    if savepath in proc_files: return
    proc_files[savepath] = True
    print("analyze_html=", url)
    
    html = open(savepath, "r", encoding="utf-8").read()
    links = enum_links (html, url)

    for link_url in links:
    # 링크가 루트 이외의 경로를 나타낸다면 무시
        if link_url.find(root_url) != 0:
            if not re.search(r".css$", link_url): continue 
        if re.search(r".(html htm)$", link_url):
            analyze_html(link_url, root_url)
            continue
        download_file(link_url)

if __name__== "__main__": 
    # URL에 있는 모든 것 다운받기
    url = "https://docs.python.org/3.8/library/"
    analyze_html(url, url)

'''
#urljoin 사용
from urllib.parse import urljoin

base = "http://example.com/html/a.html"
print(urljoin(base,"b.html")) # http://example.com/html/b.html
print(urljoin(base,"sub/c.html"))# http://example.com/html/sub/c.html
print(urljoin(base,"../index.html"))#http://example.com/index.html
#절대경로(rootdirectory),상대경로(현재directory기준 이름을붙인 경로)
print(urljoin(base,"../img/hoge.png"))#http://example.com/img/hoge.png
print(urljoin(base,"../css/hoge.css"))#http://example.com/css/hoge.css
'''