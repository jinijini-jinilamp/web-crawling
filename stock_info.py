from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

#Top종목에 있는 정보를 Sub메뉴(상한가)가져와서 xlsx파일로 정리하기
url="https://finance.naver.com/sise/"
page = urlopen(url)
soup = BeautifulSoup(page,'lxml')
topUpList=soup.find("table", id="siselist_tab_0")

#html정보를 문자열로 변경
topUpList = str(topUpList)

#pandas의 read_html로 테이블 정보 읽기
table_df_list = pd.read_html(topUpList)
print(table_df_list[0])

#데이터를 읽어서 xlsx로 저장하기
#html에서 하나의 표만 불러왔더라도 리스트안에 데이터프레임이 들어있는 형태로 나타난다. 따라서 table을 데이터프레임으로 활용하려면 무조건 인덱스로 불러주어야한다
table_df_list[0].to_excel("top stock info.xlsx", index=False ,encoding='euc-kr')