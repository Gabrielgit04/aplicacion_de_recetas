from crud import UserCrud, RecipesCrud
class User(RecipesCrud):
    def __init__(self):
        super().__init__()

class Admin(UserCrud, RecipesCrud):
    def __init__(self):
        super().__init__()

if __name__ == '__main__':
    ola = Admin()
    ola.agg()