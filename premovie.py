#개봉예정 영화 title 가지고 오기
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

url = "https://movie.naver.com/movie/running/premovie.nhn"
page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')

title = soup.find_all("dl",class_="lst_dsc")
titleList = []
for i in title:
    print(i.find("a").text)
    titleList.append(i.find("a").text)

data = {"title": titleList}
data = pd.DataFrame(data)
data.to_csv("premovie_title.csv",index=False)
print(data)