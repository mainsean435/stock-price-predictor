from dotenv import load_dotenv
import os
from datetime import timedelta

load_dotenv()

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS=os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    JWT_EXPIRATION_DELTA=timedelta(days=1)
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(days=1)


class DevConfig(Config):
    DEBUG=True
    username=os.environ.get('DEV_DB_USERNAME')
    password=os.environ.get('DEV_DB_PASSWORD')
    server=os.environ.get('DEV_DB_SERVER')
    dbname=os.environ.get('DEV_DB_DBNAME')
    SQLALCHEMY_ECHO=True
    SQLALCHEMY_DATABASE_URI=f"mysql+mysqlconnector://{username}:{password}@{server}/{dbname}"


class ProdConfig(Config):
    username=os.environ.get('PROD_DB_USERNAME')
    password=os.environ.get('PROD_DB_PASSWORD')
    server=os.environ.get('PROD_DB_SERVER')
    dbname=os.environ.get('PROD_DB_DBNAME')
    DEBUG=os.environ.get('DEBUG')
    SQLALCHEMY_ECHO=os.environ.get('ECHO')
    SQLALCHEMY_DATABASE_URI=f"mysql+mysqlconnector://{username}:{password}@{server}/{dbname}"
    SQLALCHEMY_TRACK_MODIFICATIONS=os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI='sqlite:///test.db'
    SQLALCHEMY_ECHO=False
    TESTING=True