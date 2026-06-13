import pytest
from app import create_app
from app.config import TestingConfig

@pytest.fixture
def app():
    """Create app with test config for every test."""
    app = create_app(config_class=TestingConfig)
    yield app

@pytest.fixture
def client(app):
    """Flask test client — makes HTTP calls without a real server."""
    return app.test_client()

@pytest.fixture
def app_version(app):
    """Convenience fixture to read version from app config."""
    return app.config["APP_VERSION"]