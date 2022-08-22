import os
from dotenv import load_dotenv
load_dotenv()


class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    TESTING = False


class ProductionConfig(BaseConfig):
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    pass


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
