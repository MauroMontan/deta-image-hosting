from deta import Deta
from ..config.config import Config

deta = Deta(Config.PROJECT_KEY)  # configure your Deta project 

class Drive(object):
    
    folder = drive = deta.Drive(Config.ROOT_FOLDER)

