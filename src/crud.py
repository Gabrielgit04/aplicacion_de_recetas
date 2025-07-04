from abc import ABC
from database import DataBase

"""
****************************************************
*  OPERACIONES BASICAS RELACIONADAS CON EL USUARIO:
****************************************************
"""
class UserCrud(DataBase, ABC):
    def __init__(self):
        super().__init__()

    def agg(self, _data):
        try:
            if not self.get_user("username", _data['user']) is None:
                return 456
            if not self.get_user("email", _data['email']) is None:
                return 457
            query = "INSERT INTO users (username, email, password) VALUES(?, ?, ?)"
            values = (_data['user'], _data['email'], _data['passw'])
            self.conn.execute(query, values)
            self.db.commit()
            return 111
        except Exception as e:
            print(f"ERROR: {e}")
            return 000

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

    def get_user(self, _parameter, _data):
        try:
            query = f"SELECT * FROM users WHERE {_parameter} == ?"
            value = (_data,)
            result = self.conn.execute(query, value).fetchone()
            if result is None:
                return None
            return result
        except Exception as e:
            print(f"ERROR: {e}")
            return False

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
"""
****************************************************
*  OPERACIONES BASICAS RELACIONADAS CON EL ADMIN:
****************************************************
"""
class RecipesCrud(DataBase, ABC):
    def __init__(self):
        super().__init__()

    def agg(self, _data):
        try:
            query = ("INSERT INTO recipes (title, descripcion, ingredients, steps, category, id_user, url_img) "
                     "VALUES(?, ?, ?, ?, ?, ?, ?)")
            values = (_data['title'], _data['descripcion'], _data['ingredients'], _data['steps'], _data['category'],
                      _data['id_user'], _data['url_img'])
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

    def get_recipe(self, _parametro,_title):
        try:
            query = f"SELECT * FROM recipes WHERE {_parametro} LIKE '%{_title}%'"
            result = self.conn.execute(query).fetchall()
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