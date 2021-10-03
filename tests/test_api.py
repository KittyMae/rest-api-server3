import pytest
import requests
from urllib.parse import urlencode

# @pytest.fixture
# def test_server():
#     app.run()
#     return "http://localhost:5000"

# @pytest.fixture(scope="session")
# def httpserver_listen_address()
#     return ("127.0.0.1", 5000)


def test_retrieve_histogram_check_status_code_equals_201(client):
    response = client.get("/histogram")
    
    args = urlencode({'filename': "test2.txt", 'text': "cat"})
    
    response = client.get(URL+"/retrieve-histogram?"+args)
    assert response.status_code == 201
    
    
# @pytest.mark.parametrize("path", ("/create", "/1/update", "/1/delete"))
# def test_login_required(client, path):
#     response = client.post(path)
#     assert response.headers["Location"] == "http://localhost/auth/login"
