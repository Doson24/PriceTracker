import pandas as pd
import sqlite3
from os import PathLike


class SQLite_operations:
    """
    Класс для работы с базой данных SQLite.
    """

    def __init__(self, file_path: PathLike, table_name):
        """
        Инициализация класса.

        :param file_path: Путь к файлу базы данных.
        :param table_name: Имя таблицы в базе данных.
        """
        self.path = file_path
        self.table_name = table_name

    def add_data(self, df: pd.DataFrame):
        """
        Добавление данных в таблицу.

        :param df: DataFrame с данными для добавления.
        """
        conn = sqlite3.connect(database=self.path)
        df.to_sql(self.table_name, conn, if_exists='append', index=False)
        print("Added in Database")
        conn.close()
        print("Connection closed")

    def create_table(self, conn: sqlite3.Connection):
        """
        Создание таблицы в базе данных.

        :param conn: Соединение с базой данных.
        """
        cur = conn.cursor()
        cur.execute("CREATE TABLE table_name (col1 TEXT, col2 INTEGER, col3 REAL)")
        conn.close()

    def select_All(self, table_name):
        """
        Получение всех данных из таблицы.

        :param table_name: Имя таблицы.
        :return: Все строки из таблицы.
        """
        conn = sqlite3.connect(self.path)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {table_name}")
        rows = cur.fetchall()
        conn.close()
        return rows

    def insert_row(self, columns, values):
        """
        Вставка строки в таблицу.

        :param columns: Список колонок.
        :param values: Список значений.
        """
        conn = sqlite3.connect(self.path)
        cur = conn.cursor()
        columns = ', '.join(columns)
        values_template = ', '.join(['?' for _ in values])
        sql_query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({values_template})"
        cur.execute(sql_query, list(values))
        conn.commit()
        conn.close()

    def find_unsent_records(self):
        """
        Поиск неотправленных записей.

        :return: Неотправленные записи.
        """
        conn = sqlite3.connect(self.path)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {self.table_name} WHERE sended = 0")
        rows = cur.fetchall()
        conn.close()
        return rows

    def update_sended(self, bid_number):
        """
        Обновление статуса отправки записи.

        :param id_: id записи.
        """
        conn = sqlite3.connect(self.path)
        cur = conn.cursor()
        cur.execute(f"UPDATE {self.table_name} SET sended = 1 WHERE bid_number = {bid_number}")
        conn.commit()
        conn.close()

    def is_record_created(self, date_create):
        """
        Проверка наличия записи с заданной датой создания.

        :param date_create: Дата создания.
        :return: True, если запись существует, иначе False.
        """
        conn = sqlite3.connect(self.path)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {self.table_name} WHERE date_create = '{date_create}'")
        rows = cur.fetchall()
        if len(rows) > 0:
            conn.close()
            return True
        else:
            conn.close()
            return False

    def check_bid_number(self, bid_number):
        """
        Проверка наличия записи с заданным id.

        :param id_: id.
        :return: True, если запись существует, иначе False.
        """
        conn = sqlite3.connect(self.path)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {self.table_name} WHERE bid_number = '{bid_number}'")
        rows = cur.fetchall()
        if len(rows) > 0:
            conn.close()
            return True
        else:
            conn.close()
            return False

    def check_by_name(self, title):
        """
        Проверка наличия записи с заданным названием.

        :param title: Название.
        :return: True, если запись существует, иначе False.
        """
        conn = sqlite3.connect(self.path)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {self.table_name} WHERE title = '{title}'")
        rows = cur.fetchall()
        if len(rows) > 0:
            conn.close()
            return True
        else:
            conn.close()
            return False

    def get_columns(self):
        """
        Получение названий колонок из заданной таблицы.

        :return: Список названий колонок.
        """
        conn = sqlite3.connect(self.path)
        cur = conn.cursor()
        cur.execute(f"PRAGMA table_info({self.table_name})")
        columns = [column[1] for column in cur.fetchall()]
        conn.close()
        return columns

    def select_by_datetime(self, date_time):
        """
        Получение записей, старше заданного времени.

        :param date_time: Заданное время.
        :return: Записи, старше заданного времени.
        """
        conn = sqlite3.connect(self.path)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {self.table_name} WHERE date_create > '{date_time}'")
        rows = cur.fetchall()
        conn.close()
        return rows


if __name__ == "__main__":
    path = 'C:\\Users\\user\\Desktop\\Projects\\Price_monitoring\\Price_item\\online_markets.db'
    dns = SQLite_operations(path, 'DNS')
    dns.add_data(pd.DataFrame({'data': [1, 2, 3]}))
