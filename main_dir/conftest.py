import pytest
import requests
import config

@pytest.fixture()
def post_method():
    user = {
        "name": "Nick",
        "job": "QA"
    }
    return user

@pytest.fixture()
def put_method():
    user_update = {
        "name": "Nick",
        "job": "QA Lead"
    }
    return user_update

@pytest.fixture(scope="class")
def response_first():
    response_first = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=London&appid={config.APIkey}')
    return response_first

