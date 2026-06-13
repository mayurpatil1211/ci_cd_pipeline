import os

class Config:
    APP_VERSION = os.getenv("APP_VERSION", "v1")
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    APP_VERSION = "test"

class ProductionConfig(Config):
    pass

config_map = {
    "development": DevelopmentConfig,
    "testing":     TestingConfig,
    "production":  ProductionConfig,
}

def get_config():
    env = os.getenv("FLASK_ENV", "production")
    return config_map.get(env, ProductionConfig)