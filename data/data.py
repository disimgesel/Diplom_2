class Urls:
    BASE_URL = "https://stellarburgers.nomoreparties.site"


class Endpoints:
    CREATE_USER = "/api/auth/register"
    LOGIN = "/api/auth/login"
    CHANGE_DATA_USER = "/api/auth/user"
    DELETE_USER = "/api/auth/user"
    CREATE_ORDER = "/api/orders"
    GET_ORDERS = "/api/orders"
    GET_INGREDIENTS = "/api/ingredients"


class Headers:
    headers = {"Content-Type": "application/json"}


class Ingredients:
    invalid_data_ingredients = {"ingredients": ["not_valid1", "not_valid2"]}


class UserData:
    data_valid = {
        "email": "email_valid101@yandex.ru",
        "password": "password-1"}

    data_not_valid = {
        "email": "email_not_valid101@yandex.ru",
        "password": "password-1"}

    data_double = {
        "email": "email_valid101@yandex.ru",
        "password": "password-1",
        "name": "name-1"}

    data_without_email = {
        "email": "",
        "password": "password-1",
        "name": "name-1"}

    data_without_password = {
        "email": "email_valid101@yandex.ru",
        "password": "",
        "name": "name-1"}

    data_without_name = {
        "email": "email_valid101@yandex.ru",
        "password": "password-1",
        "name": ""}
