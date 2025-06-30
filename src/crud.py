from abc import ABC
from database import DataBase

class UserCrud(DataBase, ABC):
    def __init__(self):
        super().__init__()

    def agg(self, _data):
        try:
            if self.get_user(_data['user']) is None:
                query = "INSERT INTO users (username, email, password) VALUES(?, ?, ?)"
                values = (_data['user'], _data['email'], _data['passw'])
                self.conn.execute(query, values)
                self.db.commit()
                return True
            raise Exception
        except Exception as e:
            print(f"ERROR: {e}")
            return False

    def delete(self, _data):
        try:
            query = "DELETE FROM users WHERE id == ?"
            self.conn.execute(query, (_data,))
            self.db.commit()
            return True
        except Exception as e:
            print(f"ERROR: {e}")
            return False

    def get_all(self):
        try:
            query = "SELECT * FROM users"
            result = self.conn.execute(query)
            return result.fetchall()
        except Exception as e:
            print(f"ERROR: {e}")
            return False

    def get_user(self, _username):
        try:
            query = "SELECT * FROM users WHERE username == ?"
            value = (_username,)
            result = self.conn.execute(query, value).fetchone()
            if result is None:
                return None
            return result
        except Exception as e:
            print(f"ERROR: {e}")
            return False

    def verific_user(self, _username, _password):
        try:
            query = "SELECT * FROM users WHERE username == ? and password == ?"
            value = (_username, _password)
            result = self.conn.execute(query, value).fetchone()
            if result:
                return True
            else:
                return False
        except Exception as e:
            print(f"ERROR: {e}")
            return e

    def update(self, _data):
        try:
            query = "UPDATE users SET password = ? WHERE user == ?"
            values = (_data['passw'], _data['user'])
            self.conn.execute(query, values)
            self.db.commit()
            return True
        except Exception as e:
            print(f"ERROR: {e}")
            return False

class RecipesCrud(DataBase, ABC):
    def __init__(self):
        super().__init__()

    def agg(self, _data):
        try:
            query = ("INSERT INTO recipes (title, descripcion, ingredients, steps, category, id_user) "
                     "VALUES(?, ?, ?, ?, ?, ?)")
            values = (_data['title'], _data['descrip'], _data['ingredi'], _data['steps'], _data['category'],
                      _data['id_user'])
            self.conn.execute(query, values)
            self.db.commit()
            return True
        except Exception as e:
            print(f"ERROR: {e}")
            return False

    def get_all(self):
        try:
            query = "SELECT * FROM recipes"
            result = self.conn.execute(query)
            return result.fetchall()
        except Exception as e:
            print(f"ERROR: {e}")
            return False

    def get_recipe(self, _title):
        try:
            query = "SELECT * FROM recipes WHERE title == ?"
            value = (_title,)
            result = self.conn.execute(query, value).fetchone()
            if result is None:
                return None

            return result
        except Exception as e:
            print(f"ERROR: {e}")
            return False

    def update(self, _data):
        pass

    def delete(self, _data):
        try:
            query = "DELETE FROM recipes WHERE id == ?"
            self.conn.execute(query, (_data,))
            self.db.commit()
            return True
        except Exception as e:
            print(f"ERROR: {e}")
            return False