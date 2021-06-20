# 6-2추가 과제02텍스트, 03링크 의 페이지 가져오기
import time
import lxml
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://pythonstart.github.io/web/'
start = time.time()
chromedriver = "C:\\Users\\yanghj\\Desktop\\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
driver.get(url)




# 02텍스트 가지고 오기
###해당 링크를 열고 두번째 컨텐츠 클릭
xpath02 = '/html/body/ul/a[2]'
textPage02 = driver.find_element_by_xpath(xpath02)

textPage02.click()

###해당 컨텐츠의 url로 들어가기
driver.switch_to.window(driver.window_handles[-1])  # 새탭의 다음페이지로
page02 = driver.page_source
soup02 = BeautifulSoup(page02, 'lxml')

###해당 컨텐츠를 받기
contents_obj = []
contents = soup02.find_all("p")
for i in contents:
    contents_obj.append(i.text)

###탭이동 맨앞으로
driver.switch_to.window(driver.window_handles[0])

# #03링크도 02와 같은 방법으로
xpath03 = '/html/body/ul/a[3]'
textPage03 = driver.find_element_by_xpath(xpath03)
textPage03.click()
# print(driver.window_handles)

driver.switch_to.window(driver.window_handles[-1])

page03 = driver.page_source
soup03 = BeautifulSoup(page03, 'lxml')

link_obj = []
links = soup03.find_all("a")
for j in links:
    link_obj.append(j.get('href'))

print(contents_obj)
print(link_obj)
data = {'contents': contents_obj, 'link': link_obj}
data = pd.DataFrame(data)
print(data)