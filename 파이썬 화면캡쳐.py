#화면캡쳐하기
from selenium.webdriver import Firefox, FirefoxOptions
import time
url="http://www.daum.net"
options=FirefoxOptions()
#headless ==> 웹브라우저가 나옴
options.add_argument('-headless')
browser=Firefox(options=options)
browser.get(url)
time.sleep(10)
browser.save_screenshot("d:/website.png")
browser.quit()