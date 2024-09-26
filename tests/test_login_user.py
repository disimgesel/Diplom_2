from data.data import Urls, Endpoints, UserData
import requests
import allure


class TestloginUser:

    @allure.description("Успешная авторизация под пользователем, который создан в базе данных")
    @allure.title("Авторизация под пользователем, который создан в базе данных")
    def test_login_user(self):
        response = requests.post(f"{Urls.BASE_URL}{Endpoints.LOGIN}", data=UserData.data_valid)
        assert response.status_code == 200 and response.json().get("success") == True

    @allure.description("Не успешная авторизация под пользователем с не валидным логином/паролем")
    @allure.title("Авторизация с не валидным логином/паролем")
    def test_login_user_error(self):
        response = requests.post(f"{Urls.BASE_URL}{Endpoints.LOGIN}", data=UserData.data_not_valid)
        assert response.status_code == 401 and response.json().get("success") == False
