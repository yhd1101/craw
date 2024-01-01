import requests
from bs4 import BeautifulSoup
#class . id=#

url = "https://www.naver.com/"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# 클래스가 "MediaContentsView-module__info_title___vdgEM"인 <a> 태그 선택
word = soup.select_one("#newsstand")

if word:
    print(word.text)
else:
    print("Element not found.")
