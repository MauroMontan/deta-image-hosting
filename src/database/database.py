from deta import Deta
from ..config.config import Config

deta = Deta(Config.PROJECT_KEY)  # configure your Deta project 

class Database(object):
    
    users  = deta.Base("users")
