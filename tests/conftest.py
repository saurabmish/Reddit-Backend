import pytest

from app import app as flask_app


@pytest.fixture
def app():
    """ Creates test object."""
    yield flask_app


@pytest.fixture
def client(app):
    """ Test client for the application.

    Used by tests to make application requests without running the flask
    server.

    Uses the application object (flask_app) created by the app fixture.
    """
    return app.test_client()
