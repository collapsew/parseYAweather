import requests
from bs4 import BeautifulSoup


def get_html(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 OPR/94.0.0.0'}
    response = requests.get(url, headers=headers)
    html = response.text
    return html


# noinspection PyBroadException
def get_weather_now(text):
    url = f'https://yandex.ru/pogoda/{text}'
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    print(url)
    try:

        temp = soup.find('div', class_='fact__hour-temp').get_text(strip=True)
        description = soup.find('div', class_='link__condition day-anchor i-bem').get_text(strip=True)
        print(f'Температура воздуха сейчас "{temp}\n{description}"')
    except:
        print(f'Город "{text}" не найден. Скорее всего вы сделали опечатку')


text = input('Введи город, в котором хочешь узнать погоду: ')
get_weather_now(text)