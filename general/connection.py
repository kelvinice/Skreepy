import sqlite3

from general import util
from general.util import to_bool, normalize_string
from meta.singleton import Singleton


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

        sql = ('CREATE TABLE IF NOT EXISTS master_tests('
               'id TEXT PRIMARY_KEY,'
               'test_date TEXT,'
               'tester_name TEXT,'
               'test_title TEXT'
               ')'
               )
        cursor.execute(sql)

        sql = ('CREATE TABLE IF NOT EXISTS tests('
               'id TEXT PRIMARY_KEY,'
               'master_test_id TEXT,'
               'description TEXT,'
               'overall_result TEXT,'
               'url_result TEXT,'
               'text_result TEXT,'
               'element_result TEXT,'
               'url_expected TEXT,'
               'text_expected TEXT,'
               'element_expected TEXT,'
               'FOREIGN KEY(master_test_id) REFERENCES master_tests(id)'
               ')'
               )
        cursor.execute(sql)

        sql = ('CREATE TABLE IF NOT EXISTS test_inputs('
               'id TEXT PRIMARY_KEY,'
               'test_id TEXT,'
               'tag TEXT,'
               'input_id TEXT,'
               'name TEXT,'
               'inner_html TEXT,'
               'original_value TEXT,'
               'value TEXT,'
               'class TEXT,'
               'FOREIGN KEY(test_id) REFERENCES tests(id)'
               ')'
               )
        cursor.execute(sql)

        cursor.close()

        self.close_connection()

    def master_test_already_exist(self, master_test_id) -> bool:
        sql = """
            SELECT * FROM master_tests WHERE id = ?
        """
        self.open_connection()
        cursor = self.get_cursor()

        tuple_data = (master_test_id,)
        res = cursor.execute(sql, tuple_data)
        row = res.fetchone()
        self.close_connection()

        return row is not None

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
            data["id"], data["description"], data["overall_result"]
            , result["url_after"], result["text_found"], result["element_found"]
            , expected["url_after"], expected["text_after"], expected["element_after"], data["master_test_id"])

        sql = """
            INSERT INTO tests(id,
               description,
               overall_result,
               url_result,
               text_result,
               element_result,
                url_expected,
               text_expected,
               element_expected,
               master_test_id
               )
               VALUES (?,?,?,?,?,?,?,?,?,?)
        """

        self.open_connection()
        cursor = self.get_cursor()
        cursor.execute(sql, tuple_data)
        self.commit()

        cursor.close()
        self.close_connection()

        for i in data["inputs"]:
            self.insert_inputs(data["id"], i)

    def insert_master(self, data):
        tuple_data = (
            data["master_test_id"], data["date"], data["tester"], data["title"],
        )

        sql = """
                INSERT INTO master_tests(id ,
                    test_date, tester_name, test_title
                    )
                   VALUES (?,?,?,?)
                """

        self.open_connection()
        cursor = self.get_cursor()
        cursor.execute(sql, tuple_data)
        self.commit()

        cursor.close()
        self.close_connection()

    def insert_inputs(self, test_id, input_data):
        sql = """
        INSERT INTO test_inputs(id, test_id, tag, input_id,name,inner_html,original_value,value,class) 
        VALUES (?,?,?,?,?,?,?,?,?)
        """

        tuple_data = (
            normalize_string(util.get_uuid()),
            normalize_string(test_id),
            normalize_string(input_data["tag"]),
            normalize_string(input_data["id"]),
            normalize_string(input_data["name"]),
            normalize_string(input_data["innerHTML"]),
            normalize_string(input_data["original_value"]),
            normalize_string(input_data["value"]),
            normalize_string(input_data["class"]),
        )
        self.open_connection()
        cursor = self.get_cursor()
        cursor.execute(sql, tuple_data)
        self.commit()

        cursor.close()
        self.close_connection()

    def get_input(self, test_id):
        sql = """
            SELECT * FROM test_inputs 
            WHERE test_id = ?
        """
        cursor = self.get_cursor()

        res = cursor.execute(sql, (test_id,))
        rows = res.fetchall()
        datas = []

        cursor.close()

        for row in rows:
            data = {"tag": row[2],
                    "id": row[3],
                    "class": row[8],
                    "name": row[4], "value": row[7],
                    "innerHTML": row[5],
                    "original_value": row[6],
                    }
            datas.append(data)

        return datas

    def get_master_tests(self):
        sql = """
        SELECT id,test_date,tester_name,test_title FROM master_tests
        """
        self.open_connection()
        cursor = self.get_cursor()

        res = cursor.execute(sql)
        rows = res.fetchall()
        data_list = []

        cursor.close()

        for row in rows:
            data = {
                "id": normalize_string(row[0]),
                "test_date": normalize_string(row[1]),
                "tester_name": normalize_string(row[2]),
                "test_title": normalize_string(row[3])
            }
            data_list.append(data)

        self.close_connection()
        return data_list

    def get_tests(self, master_test_id=''):
        sql = """
            SELECT 
            t.id,
            t.master_test_id,
            mt.test_date,
            mt.tester_name,
            mt.test_title,
            description,
            overall_result,
            url_result,
            text_result,
            element_result,
            url_result,
            text_result,
            element_result,
            url_expected,
            text_expected,
            element_expected
            FROM tests t JOIN master_tests mt
            on t.master_test_id = mt.id
            WHERE t.master_test_id like ?
        """
        self.open_connection()

        cursor = self.get_cursor()
        tuple_data = ('%%'+master_test_id+'%%',)
        res = cursor.execute(sql, tuple_data)
        rows = res.fetchall()
        datas = []

        cursor.close()

        for row in rows:
            inp = self.get_input(row[0])

            result = {
                "url_after": row[7],
                "text_found": to_bool(row[8]),
                "element_found": to_bool(row[9])
            }
            expected = {
                "url_after": row[10],
                "text_after": row[11],
                "element_after": row[12]
            }

            data = {
                "result": result,
                "expected": expected,
                "id": row[0],
                "master_test_id": row[1],
                "date": row[2],
                "title": row[4],
                "description": row[5],
                "inputs": inp,
                "tester": row[3],
                "overall_result": to_bool(row[6])
            }
            datas.append(data)

        self.close_connection()
        return datas
