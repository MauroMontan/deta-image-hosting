import jwt
from ..config.config import Config
from ..database.database import Database

class Auth:
    @staticmethod
    def currentUser(token:str):
        user = jwt.decode(token, key=Config.SECRET_KEY)
        
        return user
        #return Database.users.fetch({"email":user["email"]}).last


