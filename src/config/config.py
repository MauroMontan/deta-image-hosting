import os 
from dotenv import load_dotenv


load_dotenv()

class Config:
    LOCALPORT:str = str(os.getenv("LOCALPORT"))
    SECRET_KEY:str = str(os.getenv("SECRET_KEY"))
    PROJECT_KEY:str = str(os.getenv("PROJECT_KEY"))
    ROOT_FOLDER:str = str(os.getenv("ROOT_FOLDER"))



