import requests
from bs4 import BeautifulSoup

URL = 'https://flibusta.su'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 OPR/116.0.0.0'
}

#request
def get_html(url, params=''):
    response = requests.get(url, headers=HEADERS, params=params)
    return response

#2
def get_data(html, )
    bs = BeautifulSoup(html, features='html.parser')
    items = bs.find_all('div', class_='item')
    flibusta_list = []
    for item in items:
        title = item.find('div', class_='item.link').get_text(strip=True)
        flibusta_list.append({'title': title})
    return flibusta_list


#3
def parsing_flibusta():
    response = get_html(URL)
    if response.status_code == 200:
        flibusta_list2 = []
        for page in range(1,2):
