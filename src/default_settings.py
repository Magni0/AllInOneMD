import os

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        value = os.environ.get("DB_URI")

        if not value:
            raise ValueError("DB_URI is not set")

        return value

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass

class TestingConfig(Config):
    TESTING = True

enviroment = os.environ.get("FLASK_ENV")

if enviroment == "production":
    app_config = ProductionConfig()
elif enviroment == "testing":
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()