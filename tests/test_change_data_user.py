from data.data import Urls, Endpoints
import helpers
import allure
import requests


class TestChangingUserData:

    @allure.description("Успешное изменение email авторизованного пользователя")
    @allure.title("Успешное изменение email авторизованного пользователя")
    def test_change_email_without_auth(self, create_user):
        data_user = {"email": helpers.generate_user_data()["email"]}
        token = {"Authorization": create_user[1]}
        response = requests.patch(f"{Urls.BASE_URL}{Endpoints.CHANGE_DATA_USER}", headers=token, data=data_user)
        assert response.status_code == 200 and response.json()["user"]["email"] == data_user["email"]

    @allure.description("Успешное изменение password авторизованного пользователя")
    @allure.title("Успешное изменение password авторизованного пользователя")
    def test_change_password_without_auth(self, create_user):
        data_user = {"password": helpers.generate_user_data()["password"]}
        token = {"Authorization": create_user[1]}
        response = requests.patch(f"{Urls.BASE_URL}{Endpoints.CHANGE_DATA_USER}", headers=token, data=data_user)
        assert response.status_code == 200 and response.json().get("success") is True

    @allure.description("Успешное изменение name авторизованного пользователя")
    @allure.title("Успешное изменение name авторизованного пользователя")
    def test_change_name_without_auth(self, create_user):
        data_user = {"name": helpers.generate_user_data()["name"]}
        token = {"Authorization": create_user[1]}
        response = requests.patch(f"{Urls.BASE_URL}{Endpoints.CHANGE_DATA_USER}", headers=token, data=data_user)
        assert response.status_code == 200 and response.json()["user"]["name"] == data_user["name"]

    @allure.description("Не успешное изменение данных пользователя без авторизации")
    @allure.title("Не успешное изменение данных пользователя без авторизации")
    def test_change_data_not_auth(self):
        response = requests.patch(f"{Urls.BASE_URL}{Endpoints.CHANGE_DATA_USER}", data=helpers.generate_user_data())
        assert response.status_code == 401 and response.json()["message"] == "You should be authorised"
