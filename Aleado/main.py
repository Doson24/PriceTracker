import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass

from loguru import logger

from database import SQLite_operations

# Текущее время в формате timestamp
time_update = int(time.time())

cookies = {
    '_gid': 'GA1.2.1845426464.1716100025',
    '_ga_SHV75CYBKJ': 'GS1.1.1716100024.5.0.1716100026.0.0.0',
    'SU_Session': '2cbd8cbc79a9955da2a127f371ff6d71',
    'PHPSESSID': 'kb4l3kqke1ig1f3m5u6e2h82oj',
    'sess_update': '1716209736',
    '_gat_gtag_UA_37848788_1': '1',
    '_ga_K7C400WDBC': 'GS1.1.1716208453.24.1.1716209737.0.0.0',
    '_ga': 'GA1.1.1791656277.1711341310',
}

headers = {
    'authority': 'auctions.aleado.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru,en;q=0.9,ko;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_gid=GA1.2.1845426464.1716100025; _ga_SHV75CYBKJ=GS1.1.1716100024.5.0.1716100026.0.0.0; SU_Session=a5a4a49ad612c871c80e8669ff45f7a5; PHPSESSID=e6cckv6mq919qfkc3taji98q0i; sess_update=1716208489; _gat_gtag_UA_37848788_1=1; _ga=GA1.1.1791656277.1711341310; _ga_K7C400WDBC=GS1.1.1716208453.24.1.1716208621.0.0.0',
    'origin': 'https://auctions.aleado.ru',
    'referer': 'https://auctions.aleado.ru/auctions/?p=project/findlots&s&ld',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "YaBrowser";v="24.4", "Yowser";v="2.5"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 YaBrowser/24.4.0.0 Safari/537.36',
}

data = {
    's': '',
    'o': 'd',
    'vs': '20',
    'pg': '1',
    'rows': '26',
    'rudder': '',
    'date_check': '0',
    'auction_check': '1',
    'bid_number_check': '1',
    'photo_check': '1',
    'company_check': '1',
    'model_check': '1',
    'grade_check': '1',
    'year_check': '1',
    'awd_check': '',
    'transmission_check': '1',
    'displacement_check': '1',
    'mileage_check': '1',
    'inspection_check': '1',
    'color_check': '0',
    'model_type_check': '1',
    'equipment_check': '0',
    'start_price_check': '1',
    'end_price_check': '1',
    'result_check': '1',
    'scores_check': '1',
    'mrk': '7',
    'mdl_id': '592',
    'mdl[]': '592',
    'lot': '',
    'year1': '2019',
    'year2': '2021',
    'mileage1': '',
    'mileage2': '',
    'v1': '',
    'v2': '1800',
    'start1': '',
    'start2': '',
    'type': '',
    'word': '',
    'transmission': '',
    'awd': '',
    'score[]': [
        '4',
        '4.5',
        '5',
        '6',
        '7',
    ],
    'exch': 'rur',
}

@dataclass
class AuctionData:
    bid_number: str
    link: str
    auction: str
    photo: str
    company: str
    model: str
    grade: str
    year: str
    mileage: str
    inspection: str
    displacement: str
    transmission: str
    color: str
    model_type: str
    start_price: str
    end_price: str
    result: str
    scores: str
    sended: int = 0


def get_card(soup, table_rows):
    for num in range(1, len(table_rows) - 1):
        # Поиск bid_number по id
        try:
            bid_number = soup.find(id=f'bid_number_{num}').text.strip()
        except:
            continue
        try:
            link = 'https://auctions.aleado.ru' + soup.select_one(f'#photo_{num} a')['href']
        except:
            continue
        auction = soup.find(id=f'auction_{num}').text.strip()
        photo = soup.select_one(f'#photo_{num} a img')['load_src']
        company = soup.find(id=f'company_{num}').text.strip()
        model = soup.find(id=f'model_{num}').text.strip()
        grade = soup.find(id=f'grade_{num}').text.strip()
        year = soup.find(id=f'year_{num}').text.strip()
        mileage = soup.find(id=f'mileage_{num}').text.strip()
        inspection = soup.find(id=f'inspection_{num}').text.strip()
        # Обьем
        displacement = soup.find(id=f'displacement_{num}').text.strip()
        transmission = soup.find(id=f'transmission_{num}').text.strip()
        color = soup.find(id=f'color_{num}').text.strip()
        # Модель кузова
        model_type = soup.find(id=f'model_type_{num}').text.strip()
        start_price = soup.find(id=f'start_price_{num}').select_one('div').text.strip()
        end_price = soup.find(id=f'end_price_{num}').select_one('div').text.strip()
        result = soup.find(id=f'result_{num}').text.strip()
        scores = soup.find(id=f'scores_{num}').text.strip()

        yield AuctionData(bid_number, link, auction, photo, company, model, grade, year, mileage, inspection,
                          displacement, transmission, color, model_type, start_price, end_price, result, scores)


def get_data():
    # Создаем объект Path для текущего каталога
    current_dir = Path.cwd()
    dir_db = current_dir.parent
    # dir_db = current_dir.
    path_db = dir_db.joinpath('telegtam_bot/DB.db')

    db = SQLite_operations(path_db, table_name='Aleado')

    response = requests.post(
        'https://auctions.aleado.ru/auctions/?p=project/findlots&s&ld',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find(id='mainTable')
    table_rows = table.find_all('tr')
    for card in get_card(soup, table_rows):
        if not db.check_bid_number(card.bid_number):
            db.insert_row(card.__dict__.keys(), card.__dict__.values())
            logger.info(f'В БД добавлена новая запись {card.link}')


if __name__ == '__main__':
    get_data()
