import pytest
import requests
import config


@pytest.fixture(scope="class")
def response_first():
    response_first = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=London&appid={config.APIkey}')
    return response_first


user = {
    "name": "Nick",
    "job": "QA"
}

user_update = {
    "name": "Nick",
    "job": "QA Lead"
}

class TestWeatherAPITest:
    def test_get_status(self, response_first):
        assert response_first.status_code == 200

    def test_get_json(self, response_first):
        assert response_first.headers['Content-type'] == 'application/json; charset=utf-8'

    def test_city_correct_location(self, response_first):
        response_body = response_first.json()
        assert len(response_body['coord']) == 2

    def test_correct_city_name(self, response_first):
        response_body = response_first.json()
        assert response_body['name'] == 'London'

class TestReqresInAPItest:
    def test_create_user(self):
        response = requests.post("https://reqres.in/api/users", data=user)
        assert response.status_code == 201

    def test_update_user(self):
        response = requests.put("https://reqres.in/api/users/2", data=user_update)
        assert response.status_code == 200