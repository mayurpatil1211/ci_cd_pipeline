# app/__init__.py
from flask import Flask
from .config import get_config


def create_app(config_class=None):
    app = Flask(__name__)

    if config_class is None:
        config_class = get_config()
    app.config.from_object(config_class)

    from .routes import main
    app.register_blueprint(main)

    return app
