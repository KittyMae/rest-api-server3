import pytest
from urllib.request import urlopen
import requests
from io import BytesIO

from myapp import app as create_app

@pytest.fixture
def app():
    app = create_app()
    yield app

@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture(scope="session")
def httpserver_listen_address():
    return ("127.0.0.1", 8000)


# this test will pass
def test_normal_connection(httpserver):
    httpserver.expect_request("/count/").respond_with_data("WORDCOUNT")
    assert requests.get("http://localhost:8000/count/").text == "WORDCOUNT"


def test_connection_refused(httpserver):
    httpserver.stop() # stop the server explicitly
    with pytest.raises(requests.exceptions.ConnectionError):
        requests.get("http://localhost:8000/count/")



#@pytest.fixture
#def test_1(httpserver):
#    body = "Fun and more fun :-)"
#    endpoint = "/"
#    httpserver.expect_request(endpoint).respond_with_data(body)
#    with urlopen(httpserver.url_for(endpoint)) as response:
#        result = response.read().decode()
#    assert body == result
#    assert endpoint.status == 200


#@pytest.mark.parametrize()
#def
#    assert


@pytest.fixture
def setup():
	print("Start Browser")
	yield
	print("Close Browser")
	
def test_1(setup):
	print("Test 1 excuted")

	
def test_2(setup):
	print("Test 2 excuted")

	
def test_3(setup):
	print("Test 3 excuted")

def test_4(setup):
	print("Test 4 excuted")