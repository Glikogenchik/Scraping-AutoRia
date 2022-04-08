import requests
from bs4 import BeautifulSoup
import lxml

URL = 'https://auto.ria.com/newauto/marka-jeep/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
           'Chrome/96.0.4664.45 Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/'
                                                          'avif,image/webp,image/apng,*/*;q=0.8,application/'
                                                          'signed-exchange;v=b3;q=0.9'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('section', class_="proposition")

    cars = []
    for item in items:
        cars.append({
            'title': item.find('div', class_="proposition_title").get_text(strip=True),
            'link': item.find('a', class_="proposition_link").get('href'),
            'price': item.find('span', class_="green").text.strip(),

        })

    print(cars)
    print(len(cars))


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')

parse()