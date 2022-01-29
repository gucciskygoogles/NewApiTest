import pytest
import requests
from json import JSONDecoder

class TestWeatherAPITest:

    @pytest.mark.get
    @pytest.mark.xfail
    def test_get_status(self, response_first):
        assert response_first.status_code == 201

    @pytest.mark.get
    def test_get_json(self, response_first):
        try:
            assert response_first.headers['Content-type'] == 'application/json; charset=utf-8'
        except JSONDecoder:
            print('Not JSON format')

    @pytest.mark.get
    def test_city_correct_location(self, response_first):
        try:
            response_body = response_first.json()
            assert 'coord' in response_body
            assert len(response_body['coord']) == 2
        except JSONDecoder:
            print('Not JSON format')

    @pytest.mark.get
    def test_correct_city_name(self, response_first):
        try:
            response_body = response_first.json()
            assert 'name' in response_body
            assert response_body['name'] == 'London'
        except JSONDecoder:
            print('Not JSON format')

class TestReqresInAPItest:

    @pytest.mark.post
    def test_create_user(self, post_method):
        try:
            response = requests.post("https://reqres.in/api/users", data=post_method)
            assert response.status_code == 201
        except JSONDecoder:
            print('Not JSON format')

    @pytest.mark.update
    def test_update_user(self, put_method):
        try:
            response = requests.put("https://reqres.in/api/users/2", data=put_method)
            assert response.status_code == 200
        except JSONDecoder:
            print('Not JSON format')

    @pytest.mark.parametrize('users', [i for i in range(1, 11)])
    def test_get_name_of_user(self, users):
        try:
            response = requests.get(f"https://reqres.in/api/users/{users}")
            response_body = response.json()
            print(response_body['data']['first_name'])
            assert response.status_code == 200
        except JSONDecoder:
            print('Not JSON format')