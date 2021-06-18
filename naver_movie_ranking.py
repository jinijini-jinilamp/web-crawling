from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

url = "https://movie.naver.com/movie/running/current.nhn"
page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')
info_all = soup.find('ul', class_='lst_detail_t1').find_all('dl', class_='lst_dsc')
data = []

for i in info_all:
    title = i.find("a").text
    score = i.find("div", class_="star_t1").find("span", class_="num").text
    participants = i.find("div", class_="star_t1").find("span", class_="num2").find("em").text

    temp_rate = i.find("dl", class_="info_exp")
    if temp_rate is not None:
        rate = i.find("dl",class_="info_exp").find("span").text
        print(rate)
    else:
        rate = '0'
    director = list(i.find("dl", class_="info_txt1").children)[7].find("a").text
    director = director.translate({ord('\n'): "", ord('\r'): "", ord('\t'): ""})

    dict_doc = {"영화제목": title,
                "평점": score,
                "참여인원": participants,
                "예매율": rate,
                "영화감독": director}
    data.append(dict_doc)

data = pd.DataFrame(data)
data.to_csv("영화정보.csv", index=False, encoding='utf-8')
print(data)