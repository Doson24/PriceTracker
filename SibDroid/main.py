import requests
from bs4 import BeautifulSoup

cookies = {
    'edost_location': '943%7C%7C',
    'edost_location': '943%7C%7C',
    'PHPSESSID': 'WZkkdDODOSYJqXOb6dhnZDydTbtQtSsX',
    'deduplication_source': 'priceru',
    'analyticsParamsUrl': '%7B%22utm_source%22%3A%22priceru%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%22nsk%22%2C%22utm_content%22%3A%22%5Cu041d%5Cu043e%5Cu0432%5Cu043e%5Cu0441%5Cu0438%5Cu0431%5Cu0438%5Cu0440%5Cu0441%5Cu043a%22%2C%22utm_term%22%3A%221648733%22%2C%22pclid%22%3A%22e5761-171aa-de6c0%22%7D',
    '_ym_uid': '1712376787148456306',
    '_ym_d': '1712376787',
    '_ym_isad': '1',
    'BITRIX_CONVERSION_CONTEXT_s1': '%7B%22ID%22%3A3%2C%22EXPIRE%22%3A1712422740%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D',
    'telegram_start_visit_timestamp': '',
    'telegram_giveawey_close': 'Y',
    'IS_ASKED_CITY': 'asked',
    'CITY_URL': 'krasnoyarsk.sibdroid.ru',
    'BITRIX_SM_PK': 'desktop',
    'BITRIX_SM_TZ': 'Asia/Krasnoyarsk',
    'cted': 'modId%3D0q8q0l4t%3Bya_client_id%3D1712376787148456306',
    'edost_location': '943%7C%7C',
    'sessionIdID': '46e232e4c8161afd29d54e0761241ed7',
    '_ym_visorc': 'w',
    'activity': '0|-1',
    '_ga': 'GA1.1.116319504.1712384795',
    '_ga_K8TFY2G4M0': 'GS1.1.1712384794.1.0.1712384796.58.0.0',
}

headers = {
    'authority': 'krasnoyarsk.sibdroid.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru,en;q=0.9,ko;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'edost_location=943%7C%7C; edost_location=943%7C%7C; PHPSESSID=WZkkdDODOSYJqXOb6dhnZDydTbtQtSsX; deduplication_source=priceru; analyticsParamsUrl=%7B%22utm_source%22%3A%22priceru%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%22nsk%22%2C%22utm_content%22%3A%22%5Cu041d%5Cu043e%5Cu0432%5Cu043e%5Cu0441%5Cu0438%5Cu0431%5Cu0438%5Cu0440%5Cu0441%5Cu043a%22%2C%22utm_term%22%3A%221648733%22%2C%22pclid%22%3A%22e5761-171aa-de6c0%22%7D; _ym_uid=1712376787148456306; _ym_d=1712376787; _ym_isad=1; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A3%2C%22EXPIRE%22%3A1712422740%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; telegram_start_visit_timestamp=; telegram_giveawey_close=Y; IS_ASKED_CITY=asked; CITY_URL=krasnoyarsk.sibdroid.ru; BITRIX_SM_PK=desktop; BITRIX_SM_TZ=Asia/Krasnoyarsk; cted=modId%3D0q8q0l4t%3Bya_client_id%3D1712376787148456306; edost_location=943%7C%7C; sessionIdID=46e232e4c8161afd29d54e0761241ed7; _ym_visorc=w; activity=0|-1; _ga=GA1.1.116319504.1712384795; _ga_K8TFY2G4M0=GS1.1.1712384794.1.0.1712384796.58.0.0',
    'if-modified-since': 'Sat, 06 Apr 2024 06:56:19 GMT',
    'referer': 'https://krasnoyarsk.sibdroid.ru/catalog/noutbuk_apple_macbook_pro_16_2023_m3_pro_18gb_512gb_chernyy_kosmos_mrw13.html',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "YaBrowser";v="24.1", "Yowser";v="2.5"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36',
}


def get_data(url):
    response = requests.get(
        url,
        cookies=cookies,
        headers=headers,
    )
    # использование bs4
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('h1', class_='main-title').text.strip()

    wait_product = soup.find('p', class_='wait-title')
    if wait_product:
        try:
            wait_text = wait_product.text.strip().split(',')[0]
        except:
            wait_text = wait_product.text.strip()
        price = wait_text

    else:
        # получение цены
        price = soup.find('p', class_='current-price').text.strip()

    return title, price, url


if __name__ == '__main__':
    url = 'https://krasnoyarsk.sibdroid.ru/catalog/noutbuk_apple_macbook_pro_16_2023_m3_pro_18gb_512gb_chernyy_kosmos_mrw13/characteristics.html'
    title, price, url = get_data(url)

    print(title, price)
