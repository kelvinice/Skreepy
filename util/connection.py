import sqlite3
from meta.meta import Singleton


class Connection(metaclass=Singleton):
    def __init__(self):
        self.conn = None
        self.initialize_database_table()

    def open_connection(self):
        self.conn = sqlite3.connect('database/skreepyDB.db')

    def close_connection(self):
        self.conn.close()

    def get_cursor(self):
        return self.conn.cursor()

    def initialize_database_table(self):
        self.open_connection()

        cursor = self.get_cursor()

        sql = 'CREATE TABLE IF NOT EXISTS test(' \
              'id TEXT PRIMARY_KEY,' \
              'text_date TEXT,' \
              'tester_name TEXT,' \
              'test_title TEXT,' \
              'description TEXT,' \
              'overall_result TEXT,' \
              'url_result TEXT,' \
              'text_result TEXT,' \
              'element_result TEXT,' \
              'url_expected TEXT,' \
              'text_expected TEXT,' \
              'element_expected TEXT' \
              ')'
        cursor.execute(sql)

        self.close_connection()
