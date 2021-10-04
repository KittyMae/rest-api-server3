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

    # Generate 'Fake' test files
    testfiles = {"animals.txt": "mouse dog cat cow dog elephant dog camel cow camel",
                 "fruits.txt": "strawberry apple plum apricot plum cherry grapes apple plum peach"}
    for filename, data in testfiles.items():
        filepath=os.path.join(app.config['UPLOAD_FOLDER'], filename)
        with open(filepath, "w") as output_file:
            output_file.write(data)
    
    yield app

    # Teardown
    shutil.rmtree(tempdir)
    
@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()
