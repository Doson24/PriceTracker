from SibDroid.main import get_data as get_data_sb
from BigGeek.main import get_data as get_data_bg
from telegtam_bot.main import run_telegram_one_message


def run():
    url = 'https://krasnoyarsk.sibdroid.ru/catalog/noutbuk_apple_macbook_pro_16_2023_m3_pro_18gb_512gb_chernyy_kosmos_mrw13/characteristics.html'
    title, price = get_data_sb(url)
    url = 'https://biggeek.ru/products/apple-macbook-pro-16-mrw43-silver-m3-pro-12-core-gpu-18-core-18gb-512gb'
    title, price = get_data_bg(url)


if __name__ == '__main__':
    # run()
    run_telegram_one_message()
