import requests
from bs4 import BeautifulSoup


keyword = input("검색어를 입력하세요")
response = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=" + keyword )
html = responsa.text ##html 전체형태
soup = BeautifulSoup(html, 'html.parser')
links = soup.select(".news_tit") #결과로나옴

for link in links:
    title = link.text # 태그안에 텍스트 요소를 가져오기
    url = link.attrs['href'] #href 속성값 가져오기
    print(title, url )

print(links)
