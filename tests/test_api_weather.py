import pytest
import requests
from json import JSONDecoder
import allure


@allure.epic('Weather Cases')
class TestWeatherAPITest:


    @allure.description('Get correct status')
    @pytest.mark.get
    @pytest.mark.xfail
    def test_get_status(self, response_first):
        with allure.step('Получение статуса кода'):
            assert response_first.status_code == 201


    @pytest.mark.get
    def test_get_json(self, response_first):
        try:
            with allure.step('Проверка на формат данных'):
                assert response_first.headers['Content-type'] == 'application/json; charset=utf-8'
        except JSONDecoder:
            print('Not JSON format')


    @pytest.mark.get
    def test_city_correct_location(self, response_first):
        try:
            response_body = response_first.json()
            with allure.step('Проверка наличия имени в JSON'):
                assert 'coord' in response_body
            with allure.step('Проверка длинны'):
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





