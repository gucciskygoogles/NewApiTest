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

@pytest.fixture()
def register():
    user_to_register = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    return user_to_register

@pytest.fixture()
def cookies(register):
    response = requests.post("https://reqres.in/api/users/", data=register)
    cookies = response.cookies.get("__stripe_mid")
    return cookies