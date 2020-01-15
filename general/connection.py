import sqlite3
from typing import List, Dict, Union, Any

from meta.singleton import Singleton
from general.util import to_bool


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

    def test_already_exist(self, test_id) -> bool:
        sql = """
            SELECT * FROM tests WHERE id = ?
        """
        self.open_connection()
        cursor = self.get_cursor()

        tuple_data = (test_id,)
        res = cursor.execute(sql, tuple_data)
        row = res.fetchone()
        self.close_connection()

        return row is not None

    def update_test(self, data):
        sql = """
            UPDATE tests
            SET description = ?
            WHERE id = ?
        """
        tuple_data = (data["description"], data["id"])
        self.open_connection()
        cursor = self.get_cursor()
        cursor.execute(sql, tuple_data)
        self.commit()
        cursor.close()
        self.close_connection()

    def insert_test(self, data):
        result = data["result"]
        expected = data["expected"]
        tuple_data = (
            data["id"], data["date"], data["tester"], data["title"], data["description"], data["overall_result"]
            , result["url_after"], result["text_found"], result["element_found"]
            , expected["url_after"], expected["text_after"], expected["element_after"])

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
        cursor.execute(sql, tuple_data)
        self.commit()
        cursor.close()
        self.close_connection()

    def get_tests(self) -> List[Dict[str, Union[Dict[str, Any], Any]]]:
        sql = """
            SELECT * FROM tests
        """
        self.open_connection()

        cursor = self.get_cursor()

        res = cursor.execute(sql)
        rows = res.fetchall()
        datas = []

        for row in rows:
            result = {
                "url_after": row[6],
                "text_found": to_bool(row[7]),
                "element_found": to_bool(row[8])
            }
            expected = {
                "url_after": row[9],
                "text_after": row[10],
                "element_after": row[11]
            }

            data = {
                "result": result,
                "expected": expected,
                "id": row[0],
                "date": row[1],
                "title": row[3],
                "description": row[4],
                "tester": row[2],
                "overall_result": to_bool(row[5])
            }
            datas.append(data)

        cursor.close()

        self.close_connection()
        return datas
