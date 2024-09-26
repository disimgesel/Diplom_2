import random
import string


def generate_random_string(quantity):
    symbol = string.ascii_lowercase
    return "".join(random.choice(symbol) for i in range(quantity))


def generate_user_data():
    email = generate_random_string(10) + "@yandex.ru"
    password = generate_random_string(10)
    name = generate_random_string(10)
    return {
        "email": email,
        "password": password,
        "name": name
    }
