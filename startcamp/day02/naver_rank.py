import requests
import bs4

response = requests.get('https://www.naver.com/').text
soup = bs4.BeautifulSoup(response, 'html.parser')
result = soup.select('div.PM_CL_realtimeKeyword_rolling_base a.ah_a') #ID값을 먼저 찾아라, 클래스, 태그
for item in result:
    rank = item.select_one('.ah_r').text
    keyword = item.select_one('.ah_k').text
    print(f'{rank} / {keyword} ')

