from crud import UserCrud, RecipesCrud
class User(RecipesCrud):
    def __init__(self):
        super().__init__()

class Admin(UserCrud, RecipesCrud):
    def __init__(self):
        super().__init__()
