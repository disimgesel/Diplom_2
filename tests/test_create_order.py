from data.data import Urls, Endpoints, Headers, Ingredients
import allure
import requests


class TestCreateOrder:

    @allure.description("Создание заказа авторизованным пользователем с валидным ингредиентом")
    @allure.title("Создание заказа авторизованным пользователем с валидным ингредиентом")
    def test_create_order_without_auth(self, create_user, generate_data_ingredients):
        token = {"Authorization": create_user[1]}
        order_data = {"ingredients": [generate_data_ingredients[0]["_id"], generate_data_ingredients[1]["_id"]]}
        response = requests.post(f"{Urls.BASE_URL}{Endpoints.CREATE_ORDER}", headers=token, data=order_data)
        assert response.status_code == 200 and response.json().get("success") is True

    @allure.description("Создание заказа не авторизованным пользователем")
    @allure.title("Создание заказа не авторизованным пользователем")
    def test_create_order_not_auth(self, generate_data_ingredients):
        order_data = {"ingredients": [generate_data_ingredients[0]["_id"], generate_data_ingredients[1]["_id"]]}
        response = requests.post(f"{Urls.BASE_URL}{Endpoints.CREATE_ORDER}", data=order_data)
        assert response.status_code == 200 and response.json().get("success") is True

    @allure.description("Создание заказа без ингредиентов")
    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingridient(self):
        response = requests.post(f"{Urls.BASE_URL}{Endpoints.CREATE_ORDER}")
        assert response.status_code == 400 and response.json()["message"] == "Ingredient ids must be provided"

    @allure.description("Создание с не валидным хешем ингредиента")
    @allure.title("Создание с не валидным хешем ингредиента")
    def test_create_order_invalid_hash_ingridient(self):
        response = requests.post(f"{Urls.BASE_URL}{Endpoints.CREATE_ORDER}", headers=Headers.headers, json=Ingredients.invalid_data_ingredients)
        assert response.status_code == 500 and "Internal Server Error" in response.text
