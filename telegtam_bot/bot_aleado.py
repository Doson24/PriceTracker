import asyncio
import configparser
import sys
from datetime import datetime
from pathlib import Path
import pytz

from aiogram import Bot
from loguru import logger

sys.path.append(str(Path.cwd()))
sys.path.append(str(Path.cwd().parent))

from database import SQLite_operations
from Aleado.main import get_data as get_data_aleado

#Конфигурация logger
logger.add("logfile.log", format="{time} {level} {message}",
           level="INFO", rotation="500 MB")

# Достать API_TOKEN из config.ini
config = configparser.ConfigParser()
dir_conf = Path.cwd()
# dir_conf = dir_conf.parent
dir_conf = dir_conf.joinpath('config.ini')

config.read(dir_conf)
API_TOKEN = config['telegram']['API_TOKEN']
CHAT_ID = config['telegram']['CHAT_ID_ALEADO']

krasnoyarsk_tz = pytz.timezone('Asia/Krasnoyarsk')
# Создаем экземпляр бота
bot = Bot(token=API_TOKEN)

# Создаем объект Path для текущего каталога
current_dir = Path.cwd()
dir_db = current_dir

path_db = dir_db.joinpath('DB.db')
# path_db = dir_db.joinpath('data/DB.db')

db = SQLite_operations(path_db, 'Aleado')


def get_messages(start_time):
    current_time = datetime.now(krasnoyarsk_tz).strftime("%Y-%m-%d %H:%M:%S")
    logger.info(f"Запрос сообщений с {start_time} по {current_time}")

    messages = db.find_unsent_records()

    logger.info(f"Найдено {len(messages)} "
                f"новых сообщений")

    return messages


def format_order_message(bid_number, link, auction, photo, company, model, grade, year, mileage, inspection,
                          displacement, transmission, color, model_type, start_price, end_price, result, scores, sended):
    message = f"🔢 {bid_number}\n" \
                f"🔨 Аукцион: {auction}\n" \
                f"🏢 Компания: {company}\n" \
                f"🚗 Модель: {model}\n" \
                f'🔧 Модификация: {grade}\n' \
                f"📅 Год: {year}\n" \
                f"🛣️ Пробег: {mileage}\n" \
                f"🔍 Осмотр: {inspection}\n" \
                f"📏 Объем: {displacement}\n" \
                f'🔀 Коробка: {transmission}\n' \
                f'🎨 Цвет: {color}\n' \
                f'🚘 Тип кузова: {model_type}\n' \
                f'📈 Результат: {result}\n' \
                f'🏆 Оценка: {scores}\n' \
                f'🖼️ Фото: {photo}\n' \
                f'🔗 Ссылка: {link}\n' \

    return message


async def send_messages_to_chat(message):
    try:
        await bot.send_message(CHAT_ID, message, disable_notification=True, request_timeout=30)
        title = message.split('\n\n')[0]
        logger.info(f"Сообщение успешно отправлено в чат {title}")
    except Exception as e:
        logger.error(f"Ошибка при отправке сообщения в чат: {e}")


async def main():
    start_time = datetime.now(krasnoyarsk_tz).strftime("%Y-%m-%d %H:%M:%S")
    get_data_aleado()
    messages = get_messages(start_time)
    if messages:
        start_time = datetime.now(krasnoyarsk_tz).strftime("%Y-%m-%d %H:%M:%S")
    for message in messages:
        format_message = format_order_message(*message)
        await send_messages_to_chat(format_message)

        bid_number = message[0]
        db.update_sended(bid_number)

    await bot.session.close()


def run_telegram_wrapper():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()


if __name__ == '__main__':
    try:
        run_telegram_wrapper()
    except Exception as ex:
        logger.error(f"Ошибка: {ex}")
