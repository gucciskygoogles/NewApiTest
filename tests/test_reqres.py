import pytest
import requests
from json import JSONDecoder
import allure


@allure.epic('Reqres Cases')
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
            assert 'data' in response_body
            print(response_body['data']['first_name'])
            assert response.status_code == 200
        except JSONDecoder:
            print('Not JSON format')


    @pytest.xfail('Check fail')
    @pytest.mark.post
    def test_succesful_register(self, register, cookies):
        response = requests.post("https://reqres.in/api/users/", data=register)
        assert response.status_code == 201
        assert "token" in response.json(), 'No token in data'
        assert "__stripe_mid" in cookies