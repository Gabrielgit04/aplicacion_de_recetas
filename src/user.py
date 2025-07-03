from crud import UserCrud, RecipesCrud
class User(RecipesCrud):
    def __init__(self):
        super().__init__()

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

class Admin(UserCrud, RecipesCrud):
    def __init__(self):
        super().__init__()
