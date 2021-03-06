import os

class Config(object):

    """these config settings are applied no matter the enviroment.
    """

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY")

    # max file size for uploading to s3
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024

    @property
    def SQLALCHEMY_DATABASE_URI(self):

        """checks for database infomation as an enviroment variable"""

        value = os.environ.get("DB_URI")

        if not value:
            raise ValueError("DB_URI is not set")

        return value

    @property
    def AWS_ACCESS_KEY_ID(self):

        """checks if AWS_ACCESS_KEY_ID is set"""

        value = os.environ.get("AWS_ACCESS_KEY_ID")

        if not value:
            raise ValueError("AWS_ACCESS_KEY_ID is not set")

        return value

    @property
    def AWS_SECRET_ACCESS_KEY(self):

        """checks if AWS_SECRET_ACCESS_KEY is set"""

        value = os.environ.get("AWS_SECRET_ACCESS_KEY")

        if not value:
            raise ValueError("AWS_SECRET_ACCESS_KEY is not set")

        return value
    
    @property
    def AWS_S3_BUCKET(self):

        """checks if AWS_S3_BUCKET is set"""

        value = os.environ.get("AWS_S3_BUCKET")

        if not value:
            raise ValueError("AWS_S3_BUCKET is not set")

        return value

class DevelopmentConfig(Config):
    
    """applies config for dev enviroment"""

    DEBUG = True

class ProductionConfig(Config):

    """applies config for production enviroment"""

    @property
    def SECRET_KEY(self):
        
        """checks if SECRET_KEY is set"""

        value = SECRET_KEY

        if not value:
            raise ValueError("SECRET_KEY is not set")
        
        return value

class TestingConfig(Config):

    """applies config for testing enviroment"""

    TESTING = True

# gets the enviroment
enviroment = os.environ.get("FLASK_ENV")

# calls config for type on env: defaults to development
if enviroment == "production":
    app_config = ProductionConfig()
elif enviroment == "testing":
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()