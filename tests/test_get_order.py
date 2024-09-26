from data.data import Urls, Endpoints
import allure
import requests


class TestGetOrder:

    @allure.description("Получение заказов авторизованного пользователя")
    @allure.title("Получение заказов авторизованного пользователя")
    def test_get_order_user_without_auth(self, create_user, generate_data_ingredients):
        token = {"Authorization": create_user[1]}
        order_data = {"ingredients": [generate_data_ingredients[0]["_id"], generate_data_ingredients[1]["_id"]]}
        requests_create_order = requests.post(f"{Urls.BASE_URL}{Endpoints.CREATE_ORDER}", headers=token, data=order_data)
        response_get_order = requests.get(f"{Urls.BASE_URL}{Endpoints.GET_ORDERS}", headers=token)
        assert response_get_order.status_code == 200 and response_get_order.json()["orders"][0]["number"] == requests_create_order.json()["order"]["number"]

    @allure.description("Получение заказов неавторизованного пользователя")
    @allure.title("Получение заказов неавторизованного пользователя")
    def test_get_order_user_not_auth(self):
        response = requests.get(f"{Urls.BASE_URL}{Endpoints.GET_ORDERS}")
        assert response.status_code == 401 and response.json()["message"] == "You should be authorised"
