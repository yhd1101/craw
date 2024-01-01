import requests
from bs4 import BeautifulSoup
#종목 코드 리스트
codes = [
    '005930',
    '000660',
    '035720'

]
for code in codes:
    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    price = soup.select_one("#_nowVal").text
    high = soup.select_one("#_high").text
    price = price.replace(',', '') #숫자로 교
    high = high.replace(',', '')
    print(price)
    print(high)