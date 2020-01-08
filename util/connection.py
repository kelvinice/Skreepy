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

    def commit(self):
        self.conn.commit()

    def initialize_database_table(self):
        self.open_connection()

        cursor = self.get_cursor()

        sql = ('CREATE TABLE IF NOT EXISTS tests('
               'id TEXT PRIMARY_KEY,'
               'test_date TEXT,'
               'tester_name TEXT,'
               'test_title TEXT,'
               'description TEXT,'
               'overall_result TEXT,'
               'url_result TEXT,'
               'text_result TEXT,'
               'element_result TEXT,'
               'url_expected TEXT,'
               'text_expected TEXT,'
               'element_expected TEXT'
               ')'
               )
        cursor.execute(sql)
        cursor.close()

        self.close_connection()

    def insert_test(self,data):
        result = data["result"]
        expected = data["expected"]
        tuple = (data["id"], data["date"],data["tester"],data["title"],data["description"], data["overall_result"]
                 ,result["url_after"],result["text_found"],result["element_found"]
                 ,expected["url_after"],expected["text_after"],expected["element_after"])
        print(tuple)
        sql = """
            INSERT INTO tests(id ,test_date,
               tester_name,
               test_title,
               description,
               overall_result,
               url_result,
               text_result,
               element_result,
                url_expected,
               text_expected,
               element_expected)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
        """
        self.open_connection()
        cursor = self.get_cursor()
        cursor.execute(sql,tuple)
        self.commit()
        cursor.close()
        self.close_connection()

    def get_tests(self):
        sql = """
            SELECT * FROM tests
        """

