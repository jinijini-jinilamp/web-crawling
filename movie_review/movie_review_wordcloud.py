from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import os
from wordcloud import WordCloud
import numpy as np
from PIL import Image
from matplotlib import rc
import matplotlib.pyplot as plt

all_comments = []
url="https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=132623&target=after&page="

for i in range(1,51):
  all_url = url + str(i)
  page = urlopen(all_url)
  soup = BeautifulSoup(page,'lxml')
  comment_all = soup.find_all("td",class_="title")

  for j in comment_all:
    comment = list(j)[6].strip()
    all_comments.append(comment)

#파일 만들기
dict_doc={"text":all_comments}
doc = pd.DataFrame(dict_doc)
doc.to_csv("캡틴마블리뷰.csv", index=False, encoding='utf-8')

os.listdir(os.getcwd())

#워드클라우드
f=open("캡틴마블리뷰.csv", encoding='utf-8')
text = f.read()
f.close()
rc('font', family='NanumGothic')

wcloud = WordCloud('./data/D2Coding.ttf',
                   #stopwords=["진짜","그냥","영화"],
                   max_words=1000,
                   relative_scaling = 0.5).generate(text)

plt.figure(figsize=(12,12))
plt.imshow(wcloud, interpolation='bilinear')
plt.axis("off")