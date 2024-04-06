import requests
from bs4 import BeautifulSoup

cookies = {
    'spid': '1694193563990_5315e21b1a92417e316d4e5f97f6ee1a_pr6wu9pdftebhvev',
    '_ym_uid': '1694193567338560044',
    'device_id': 'dedecd9b-4e6b-11ee-b8b7-0242ac110002',
    'isOldUser': 'true',
    'adspire_uid': 'AS.832525504.1694193570',
    'ssaid': 'df5bd9f0-4e6b-11ee-8e68-e9c0a3c8a419',
    '_sa': 'SA1.dbdd7ebd-8456-4bda-8fce-4b33bd712e77.1694193571',
    'rrpvid': '110629721360177',
    'uxs_uid': 'e1669e10-4e6b-11ee-9633-ffc2f718c67b',
    '_gpVisits': '{"isFirstVisitDomain":true,"idContainer":"10002472"}',
    'rcuid': '64fb57a7136f21673a49ebe9',
    'flocktory-uuid': 'f7c91ee7-3620-406b-9fe6-5cca1af48f7e-4',
    'adid': '169419357619114',
    'tmr_lvid': 'c2fdac4d2af5dbcd9d6f52f0b4a9c674',
    'tmr_lvidTS': '1694329746378',
    'adtech_uid': '67d1d051-c7a4-4788-9ce1-b27a491e95de%3Amegamarket.ru',
    'top100_id': 't1.6795753.429616263.1694329746491',
    'viewType': 'grid',
    '__ttl__widget__ui': '1701504338494-0d10766772d7',
    'last_visit': '1704851708942%3A%3A1704876908942',
    't3_sid_6795753': 's1.1079573667.1704876908938.1704876932326.39.13',
    # 'sbermegamarket_token': 'd0bec085-25e8-4e81-84a6-a35598617606',
    # 'ecom_token': 'd0bec085-25e8-4e81-84a6-a35598617606',
    '_ym_d': '1710063238',
    '_gcl_au': '1.1.1111577509.1711267078',
    'adspire_last_order': '20669169341',
    # 'sbermegamarket_token': 'd0bec085-25e8-4e81-84a6-a35598617606',
    # 'ecom_token': 'd0bec085-25e8-4e81-84a6-a35598617606',
    '_gid': 'GA1.2.927031011.1712304491',
    'domain_sid': 'GIO4KFGS_ZfF-P0brSk10%3A1712304493141',
    'tmr_detect': '0%7C1712316411429',
    'st_uid': '7f71d4decaafcb8b454b7efd40d8e4a4',
    'rrlevt': '1712376107692',
    '_ym_isad': '1',
    'atm_closer': '%7B%22id%22%3A12938%2C%22mid%22%3A19066%2C%22aid%22%3A%22AS.832525504.1694193570%22%2C%22cookie_time%22%3A1712377733511%2C%22priority%22%3A0%2C%22webid%22%3A%224804270%22%2C%22uid%22%3A%2242sbi7442zrp0qh65kk76juyw3v7xw2e%22%7D',
    'spsc': '1712384039023_649bd51debafff65b059d6503282d746_0d4e0eb9c92181c656f0cb950dff1b59a3402473b747382c8fc1bc9ef31a9efa',
    '__zzatw-smm': 'MDA0dC0cTHtmcDhhDHEWTT17CT4VHThHKHIzd2Vcch8dHw0UJRAOCH9jIhg+bmlWf3VXLwkqPWx0MGFRUUtiDxwXMlxOe3NdZxBEQE1HQnR0Kz5tIV9LXCdMWElraWJRNF0tQUpPJQp0OWV2EA==7Jcc9A==',
    'region_info': '%7B%22displayName%22%3A%22%D0%9A%D0%A0%D0%90%D0%A1%D0%9D%D0%9E%D0%AF%D0%A0%D0%A1%D0%9A%D0%98%D0%99%20%D0%9A%D0%A0%D0%90%D0%99%22%2C%22kladrId%22%3A%222400000000000%22%2C%22isDeliveryEnabled%22%3Atrue%2C%22geo%22%3A%7B%22lat%22%3A56.023831%2C%22lon%22%3A92.862011%7D%2C%22id%22%3A%2224%22%7D',
    '__tld__': 'null',
    '_ga': 'GA1.2.477358907.1694193570',
    'address_info': '%7B%22addressId%22%3A%222gis_985798073693860%22%2C%22full%22%3A%22%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D1%8F%D1%80%D1%81%D0%BA%D0%B8%D0%B9%20%D0%BA%D1%80%D0%B0%D0%B9%2C%20%D0%96%D0%B5%D0%BB%D0%B5%D0%B7%D0%BD%D0%BE%D0%B3%D0%BE%D1%80%D1%81%D0%BA%2C%20%D1%83%D0%BB%D0%B8%D1%86%D0%B0%20%D0%9C%D0%B0%D1%8F%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%BE%D0%B3%D0%BE%2C%201%22%2C%22geo%22%3A%7B%22lon%22%3A93.53156%2C%22lat%22%3A56.257874%7D%7D',
    '_ga_VD1LWDPWYX': 'GS1.2.1712393549.89.1.1712393564.0.0.0',
    '_ga_W49D2LL5S1': 'GS1.1.1712393549.134.1.1712393577.32.0.0',
    # 'cfidsw-smm': 'olo2JEAsfEX6yDsKK9a88AgEQUk7iHQIUjdZ8qH71Am2hXlxAX3YsGhB0mX+pfHwD6U7mssMxj6yWkZNqjS/7HKxuqVFj0QhyiTCkG+++GmaPrLuz/X/8wrSKArwRZHKwvHT0Zz2psVnTZ/hFUp8zUbIOfNDMeDQEYs5zdQf',
    # 'cfidsw-smm': 'olo2JEAsfEX6yDsKK9a88AgEQUk7iHQIUjdZ8qH71Am2hXlxAX3YsGhB0mX+pfHwD6U7mssMxj6yWkZNqjS/7HKxuqVFj0QhyiTCkG+++GmaPrLuz/X/8wrSKArwRZHKwvHT0Zz2psVnTZ/hFUp8zUbIOfNDMeDQEYs5zdQf',
}

headers = {
    'authority': 'megamarket.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru,en;q=0.9,ko;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'spid=1694193563990_5315e21b1a92417e316d4e5f97f6ee1a_pr6wu9pdftebhvev; _ym_uid=1694193567338560044; device_id=dedecd9b-4e6b-11ee-b8b7-0242ac110002; isOldUser=true; adspire_uid=AS.832525504.1694193570; ssaid=df5bd9f0-4e6b-11ee-8e68-e9c0a3c8a419; _sa=SA1.dbdd7ebd-8456-4bda-8fce-4b33bd712e77.1694193571; rrpvid=110629721360177; uxs_uid=e1669e10-4e6b-11ee-9633-ffc2f718c67b; _gpVisits={"isFirstVisitDomain":true,"idContainer":"10002472"}; rcuid=64fb57a7136f21673a49ebe9; flocktory-uuid=f7c91ee7-3620-406b-9fe6-5cca1af48f7e-4; adid=169419357619114; tmr_lvid=c2fdac4d2af5dbcd9d6f52f0b4a9c674; tmr_lvidTS=1694329746378; adtech_uid=67d1d051-c7a4-4788-9ce1-b27a491e95de%3Amegamarket.ru; top100_id=t1.6795753.429616263.1694329746491; viewType=grid; __ttl__widget__ui=1701504338494-0d10766772d7; last_visit=1704851708942%3A%3A1704876908942; t3_sid_6795753=s1.1079573667.1704876908938.1704876932326.39.13; sbermegamarket_token=d0bec085-25e8-4e81-84a6-a35598617606; ecom_token=d0bec085-25e8-4e81-84a6-a35598617606; _ym_d=1710063238; _gcl_au=1.1.1111577509.1711267078; adspire_last_order=20669169341; sbermegamarket_token=d0bec085-25e8-4e81-84a6-a35598617606; ecom_token=d0bec085-25e8-4e81-84a6-a35598617606; _gid=GA1.2.927031011.1712304491; domain_sid=GIO4KFGS_ZfF-P0brSk10%3A1712304493141; tmr_detect=0%7C1712316411429; st_uid=7f71d4decaafcb8b454b7efd40d8e4a4; rrlevt=1712376107692; _ym_isad=1; atm_closer=%7B%22id%22%3A12938%2C%22mid%22%3A19066%2C%22aid%22%3A%22AS.832525504.1694193570%22%2C%22cookie_time%22%3A1712377733511%2C%22priority%22%3A0%2C%22webid%22%3A%224804270%22%2C%22uid%22%3A%2242sbi7442zrp0qh65kk76juyw3v7xw2e%22%7D; spsc=1712384039023_649bd51debafff65b059d6503282d746_0d4e0eb9c92181c656f0cb950dff1b59a3402473b747382c8fc1bc9ef31a9efa; __zzatw-smm=MDA0dC0cTHtmcDhhDHEWTT17CT4VHThHKHIzd2Vcch8dHw0UJRAOCH9jIhg+bmlWf3VXLwkqPWx0MGFRUUtiDxwXMlxOe3NdZxBEQE1HQnR0Kz5tIV9LXCdMWElraWJRNF0tQUpPJQp0OWV2EA==7Jcc9A==; region_info=%7B%22displayName%22%3A%22%D0%9A%D0%A0%D0%90%D0%A1%D0%9D%D0%9E%D0%AF%D0%A0%D0%A1%D0%9A%D0%98%D0%99%20%D0%9A%D0%A0%D0%90%D0%99%22%2C%22kladrId%22%3A%222400000000000%22%2C%22isDeliveryEnabled%22%3Atrue%2C%22geo%22%3A%7B%22lat%22%3A56.023831%2C%22lon%22%3A92.862011%7D%2C%22id%22%3A%2224%22%7D; __tld__=null; _ga=GA1.2.477358907.1694193570; address_info=%7B%22addressId%22%3A%222gis_985798073693860%22%2C%22full%22%3A%22%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D1%8F%D1%80%D1%81%D0%BA%D0%B8%D0%B9%20%D0%BA%D1%80%D0%B0%D0%B9%2C%20%D0%96%D0%B5%D0%BB%D0%B5%D0%B7%D0%BD%D0%BE%D0%B3%D0%BE%D1%80%D1%81%D0%BA%2C%20%D1%83%D0%BB%D0%B8%D1%86%D0%B0%20%D0%9C%D0%B0%D1%8F%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%BE%D0%B3%D0%BE%2C%201%22%2C%22geo%22%3A%7B%22lon%22%3A93.53156%2C%22lat%22%3A56.257874%7D%7D; _ga_VD1LWDPWYX=GS1.2.1712393549.89.1.1712393564.0.0.0; _ga_W49D2LL5S1=GS1.1.1712393549.134.1.1712393577.32.0.0; cfidsw-smm=olo2JEAsfEX6yDsKK9a88AgEQUk7iHQIUjdZ8qH71Am2hXlxAX3YsGhB0mX+pfHwD6U7mssMxj6yWkZNqjS/7HKxuqVFj0QhyiTCkG+++GmaPrLuz/X/8wrSKArwRZHKwvHT0Zz2psVnTZ/hFUp8zUbIOfNDMeDQEYs5zdQf; cfidsw-smm=olo2JEAsfEX6yDsKK9a88AgEQUk7iHQIUjdZ8qH71Am2hXlxAX3YsGhB0mX+pfHwD6U7mssMxj6yWkZNqjS/7HKxuqVFj0QhyiTCkG+++GmaPrLuz/X/8wrSKArwRZHKwvHT0Zz2psVnTZ/hFUp8zUbIOfNDMeDQEYs5zdQf',
    'referer': 'https://allshops.me/',
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
    response = requests.get(url, cookies=cookies, headers=headers)
    # использование bs4
    soup = BeautifulSoup(response.text, 'html.parser')
    # получение цены
    all_offers = soup.find('a', class_='more-offers-button offers-info__more-offers-button-wrapper').text.strip()
    price = all_offers.split('от')[-1]
    title = soup.find('h1', itemprop_='name').text.strip()
    return title, price, url


if __name__ == '__main__':
    url = 'https://megamarket.ru/catalog/details/noutbuk-apple-macbook-pro-16-162-m3-pro-18-512gb-space-black-mrw13-eu-keyboard-100061721552/'
    print(get_data(url))
