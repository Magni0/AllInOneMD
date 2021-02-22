import os

class Config(object):

    """these config settings are applied no matter the enviroment.
    """

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")

    @property
    def SQLALCHEMY_DATABASE_URI(self):

        """gets the database infomation from the .env file
        """

        value = os.environ.get("DB_URI")

        if not value:
            raise ValueError("DB_URI is not set")

        return value

class DevelopmentConfig(Config):
    
    """applies config for dev enviroment
    """

    DEBUG = True

class ProductionConfig(Config):

    """applies config for production enviroment
    """

    @property
    def JWT_SECRET_KEY(self):
        
        """gets JWT_SECRET_KEY from .env
        """

        value = JWT_SECRET_KEY

        if not value:
            raise ValueError("JWT Secret Key is not set")
        
        return value

class TestingConfig(Config):

    """applies config for testing enviroment
    """

    TESTING = True

enviroment = os.environ.get("FLASK_ENV")

if enviroment == "production":
    app_config = ProductionConfig()
elif enviroment == "testing":
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()