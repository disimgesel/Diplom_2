from data.data import Urls, Endpoints, UserData
import helpers
import pytest
import requests
import allure


class TestCreateUser:

    @allure.description("Создание нового пользователя c валидными параметрами")
    @allure.title("Создание нового пользователя")
    def test_create_new_user_success(self):
        response = requests.post(f"{Urls.BASE_URL}{Endpoints.CREATE_USER}", data=helpers.generate_user_data())
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.description("Создание пользователя, параметры которого уже дублируют созданного")
    @allure.title("Создание пользователя который уже создан в базе данных")
    def test_create_double_user_fail(self):
        response = requests.post(f"{Urls.BASE_URL}{Endpoints.CREATE_USER}", data=UserData.data_double)
        assert response.status_code == 403 and "User already exists" in response.text

    @allure.description("Создание пользователя с не валидными данными")
    @allure.title("Создание пользователя с не валидными данными")
    @pytest.mark.parametrize("user_data", [UserData.data_without_email, UserData.data_without_password, UserData.data_without_name])
    def test_create_user_invalid_data(self, user_data):
        response = requests.post(f"{Urls.BASE_URL}{Endpoints.CREATE_USER}", data=user_data)
        assert response.status_code == 403 and "Email, password and name are required fields" in response.text
