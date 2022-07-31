import os

class Config:
    ENV = 'development'
    DEBUG = True
    #SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(24))
    SECRET_KEY="admin"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:" + SECRET_KEY + "@localhost/db"
