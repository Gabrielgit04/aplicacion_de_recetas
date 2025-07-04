import sqlite3
from abc import ABC, abstractmethod

class DataBase(ABC):
    def __init__(self):
        self.db = sqlite3.connect("db/AASSDD.db")
        self.conn = self.db.cursor()

    def db_init(self):
        try:
            query = ("CREATE TABLE IF NOT EXISTS users "
                     "(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "
                     "username VARCHAR(15),"
                     "email VARCHAR(20),"
                     "password VARCHAR(15))")

            query_2 = ("CREATE TABLE IF NOT EXISTS recipes "
                       "(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                       "title TEXT,"
                       "descripcion TEXT,"
                       "ingredients TEXT,"
                       "steps TEXT,"
                       "category TEXT,"
                       "id_user TEXT NOT NULL,"
                       "url_img TEXT)")
            self.conn.execute(query)
            self.conn.execute(query_2)
            self.db.commit()
            self.db.close()
        except Exception as e:
            print(f"ERROR: {e}")

    @abstractmethod
    def agg(self, data):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def delete(self, _data):
        pass

    @abstractmethod
    def update(self, _data):
        pass