import requests
from bs4 import BeautifulSoup

keyword = input("검색어를 입력하세요: ")
lastPage = input("마지막페이지 입력")
pageNum = 1
for i in range(1, int(lastPage) * 10, 10): #1 11, 31 이런식 1페이지는 1 2페이지는 21 임
    print(f"{pageNum}페이지 입니다=======")
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={i}")
    html = response.text  # 오타 수정: response, not responsa
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select(".news_tit")  # 결과로 나옴

    for link in links:
        title = link.text  # 태그 안에 텍스트 요소를 가져오기
        url = link.attrs['href']  # href 속성값 가져오기
        print(title, url)
    pageNum = pageNum +1
