import os
import tempfile
import shutil

import pytest

from app import create_app

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # Setup
    tempdir = tempfile.mkdtemp(prefix="rest-api-server-")
    app = create_app({"TESTING": True, "UPLOAD_FOLDER": tempdir})
    
    yield app

    # Teardown
    shutil.rmtree(tempdir)
    
@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()
