#ȭ��ĸ���ϱ�
from selenium.webdriver import Firefox, FirefoxOptions
import time
url="http://www.daum.net"
options=FirefoxOptions()
#headless ==> ���������� ����
options.add_argument('-headless')
browser=Firefox(options=options)
browser.get(url)
time.sleep(10)
browser.save_screenshot("d:/website.png")
browser.quit()