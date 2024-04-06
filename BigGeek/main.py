import requests
from bs4 import BeautifulSoup

cookies = {
    '_ym_uid': '1699800975162323609',
    '_ym_d': '1699800975',
    'adspire_uid': 'AS.1099583928.1699800975',
    '_rc_uid': '9fa7c1e7337325ae1a1de4b7950e5d82',
    'rrpvid': '805781107707526',
    'rcuid': '65f27c522878efb2888666ad',
    '_userGUID': '0:ltqq99op:2lgh2d2R1a8QehS1ILOXNvksLxew5ap~',
    'PHPSESSID': 'f4a6a3599e313f1c685de430b9c97e7f',
    '_gid': 'GA1.2.442251125.1712376357',
    '_ym_isad': '1',
    '_rc_sess': 'ef2182aa-e663-4e6b-bdab-a9710377a8f1',
    'Duuid': 'c2002280-6e61-4dea-b987-227a840695cb',
    'browsed_products': '19891%2C23695',
    'Fuuid': 'c2002280-6e61-4dea-b987-227a840695cb,1712384948',
    '_ym_visorc': 'b',
    '_ga': 'GA1.2.1173770057.1710390355',
    '_gat_gtag_UA_71733116_1': '1',
    'dSesn': '16bb29e0-37c1-7304-8e30-84f0c0af88fd',
    '_dvs': '0:lunrzo3g:wjg0MmpxsZPwdQZbciA3DiUh8_E9yHqP',
    'digi_uc': 'W1sidiIsIjIzNjk1IiwxNzEyMzg4NjUyMTk1XSxbInN2IiwiMTczMzgiLDE3MTIzNzY0ODI1NzddLFsic3YiLCIxOTI5NiIsMTcxMjM3NjQ3NzQxNF0sWyJzdiIsIjE1MzQxIiwxNzEyMzc2NDAxMzE3XSxbInN2IiwiMjM2ODgiLDE3MTIzNzYzODg3MTNdLFsic3YiLCIxMjY5NyIsMTcxMjM3NjM2NjI5NF1d',
    '_ga_5TGXE8M4R1': 'GS1.1.1712388649.5.1.1712388653.56.0.0',
    'Dsign': 'y',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru,en;q=0.9,ko;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': '_ym_uid=1699800975162323609; _ym_d=1699800975; adspire_uid=AS.1099583928.1699800975; _rc_uid=9fa7c1e7337325ae1a1de4b7950e5d82; rrpvid=805781107707526; rcuid=65f27c522878efb2888666ad; _userGUID=0:ltqq99op:2lgh2d2R1a8QehS1ILOXNvksLxew5ap~; PHPSESSID=f4a6a3599e313f1c685de430b9c97e7f; _gid=GA1.2.442251125.1712376357; _ym_isad=1; _rc_sess=ef2182aa-e663-4e6b-bdab-a9710377a8f1; Duuid=c2002280-6e61-4dea-b987-227a840695cb; browsed_products=19891%2C23695; Fuuid=c2002280-6e61-4dea-b987-227a840695cb,1712384948; _ym_visorc=b; _ga=GA1.2.1173770057.1710390355; _gat_gtag_UA_71733116_1=1; dSesn=16bb29e0-37c1-7304-8e30-84f0c0af88fd; _dvs=0:lunrzo3g:wjg0MmpxsZPwdQZbciA3DiUh8_E9yHqP; digi_uc=W1sidiIsIjIzNjk1IiwxNzEyMzg4NjUyMTk1XSxbInN2IiwiMTczMzgiLDE3MTIzNzY0ODI1NzddLFsic3YiLCIxOTI5NiIsMTcxMjM3NjQ3NzQxNF0sWyJzdiIsIjE1MzQxIiwxNzEyMzc2NDAxMzE3XSxbInN2IiwiMjM2ODgiLDE3MTIzNzYzODg3MTNdLFsic3YiLCIxMjY5NyIsMTcxMjM3NjM2NjI5NF1d; _ga_5TGXE8M4R1=GS1.1.1712388649.5.1.1712388653.56.0.0; Dsign=y',
    'Referer': 'https://biggeek.ru/products?keyword=Macbook&digiSearch=true&term=%D0%BD%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA%20apple%20macbook%20pro%2016%2016%20m3%20pro&params=%7Csort%3DPRICE_ASC',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "YaBrowser";v="24.1", "Yowser";v="2.5"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


def get_data(url):
    response = requests.get(
        url,
        cookies=cookies,
        headers=headers,
    )
    # использование bs4
    soup = BeautifulSoup(response.text, 'html.parser')
    # получение цены
    price = soup.find('span', class_='price cart-modal-count').text.strip()
    title = soup.find('h1', class_='produt-section__title').text.strip()
    return title, price, url


if __name__ == '__main__':
    url = 'https://biggeek.ru/products/apple-macbook-pro-16-mrw43-silver-m3-pro-12-core-gpu-18-core-18gb-512gb'
    title, price, url = get_data(url)
    print(title, price)
