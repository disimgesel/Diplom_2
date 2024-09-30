from data.data import Urls, Endpoints
import helpers
import pytest
import requests


@pytest.fixture(scope="function")
def create_user():
    data_user = helpers.generate_user_data()
    data_login = data_user.copy()
    del data_login["name"]
    response = requests.post(f"{Urls.BASE_URL}{Endpoints.CREATE_USER}", data=data_user)
    token = response.json()["accessToken"]
    yield response, token, data_user, data_login
    requests.delete(f"{Urls.BASE_URL}{Endpoints.DELETE_USER}", headers={'Authorization': f'{token}'})


@pytest.fixture()
def generate_data_ingredients():
    response = requests.get(f"{Urls.BASE_URL}{Endpoints.GET_INGREDIENTS}")
    return response.json()['data']
