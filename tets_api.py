import requests
import config
import unittest

user = {
    "name": "Nick",
    "job": "QA"
}

user_update = {
    "name": "Nick",
    "job": "QA Lead"
}

class WeatherAPITest(unittest.TestCase):
    def test_get_status(self):
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=London&appid={config.APIkey}')
        assert response.status_code == 200

    def test_get_json(self):
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=London&appid={config.APIkey}')
        assert response.headers['Content-type'] == 'application/json; charset=utf-8'

    def test_city_correct_location(self):
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=London&appid={config.APIkey}')
        response_body = response.json()
        assert len(response_body['coord']) == 2

    def test_correct_city_name(self):
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=London&appid={config.APIkey}')
        response_body = response.json()
        assert response_body['name'] == 'London'

class ReqresInAPItest(unittest.TestCase):
    def test_create_user(self):
        response = requests.post("https://reqres.in/api/users", data=user)
        assert response.status_code == 201

    def test_update_user(self):
        response = requests.put("https://reqres.in/api/users/2", data=user_update)
        assert response.status_code == 200