import requests
import config
import pytest
import unittest

class APITest(unittest.TestCase):
    def test_get_status(self):
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=London&appid={config.APIkey}')
        assert response.status_code == 200
