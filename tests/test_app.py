# tests/test_app.py  ← update to use create_app()
from app import create_app
from app.config import TestingConfig

def test_app_creates_successfully():
    app = create_app(config_class=TestingConfig)
    assert app is not None

def test_app_is_in_testing_mode():
    app = create_app(config_class=TestingConfig)
    assert app.config["TESTING"] is True

def test_app_version_set():
    app = create_app(config_class=TestingConfig)
    assert app.config["APP_VERSION"] == "test"