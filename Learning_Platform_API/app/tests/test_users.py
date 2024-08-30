from http import HTTPStatus
import requests


ENDPOINT = "http://127.0.0.1:5000"


def correct_user_payload():
    return {
        "first_name": "Sergey",
        "last_name": "Sidorov",
        "phone": "+7999999999999",
        "email": "test@test.ru",
    }


def test_user_creating():
    payload = correct_user_payload()

    # Получение ответа от POST запроса
    create_response = requests.post(f"{ENDPOINT}/users/create", json=payload)

    # Тест на верный статус ответа
    assert create_response.status_code == HTTPStatus.CREATED

    # Распаковка JSON ответа
    user_data = create_response.json()
    user_id = user_data["id"]

    # Сверка данных из первоначальной отправки и вернувшегося
    assert user_data["first_name"] == payload["first_name"]
    assert user_data["last_name"] == payload["last_name"]
    assert user_data["phone"] == payload["phone"]
    assert user_data["email"] == payload["email"]

    # Получение ответа от GET запроса
    create_response_2 = requests.get(f"{ENDPOINT}/users/{user_id}")

    # Сверка данных из первоначальной отправки и вернувшегося второго запроса
    assert create_response_2.json()["first_name"] == payload["first_name"]
    assert create_response_2.json()["last_name"] == payload["last_name"]
    assert create_response_2.json()["phone"] == payload["phone"]
    assert create_response_2.json()["email"] == payload["email"]


def test_user_create_with_wrong_data():
    payload_with_wrong_phone = {
        "first_name": "Sergey",
        "last_name": "Sidorov",
        "phone": "89388",
        "email": "test@test.ru",
    }
    payload_with_wrong_email = {
        "first_name": "Sergey",
        "last_name": "Sidorov",
        "phone": "+7999999999999",
        "email": "test345",
    }

    create_response_with_wrong_phone = requests.post(
        f"{ENDPOINT}/users/create", json=payload_with_wrong_phone
    )

    create_response_with_wrong_email = requests.post(
        f"{ENDPOINT}/users/create", json=payload_with_wrong_email
    )
    assert create_response_with_wrong_phone.status_code == HTTPStatus.BAD_REQUEST
    assert create_response_with_wrong_email.status_code == HTTPStatus.BAD_REQUEST


def test_get_user_history():
    payload = correct_user_payload()
    create_response = requests.post(f"{ENDPOINT}/users/create", json=payload)
    assert create_response.status_code == HTTPStatus.CREATED
    user_data = create_response.json()
    user_id = user_data["id"]
    create_response_2 = requests.get(f"{ENDPOINT}/users/{user_id}/history")
    assert isinstance(create_response_2.json()["history"], list)


def test_leaderboard_table():
    payload = {"type": "table"}
    create_response = requests.get(f"{ENDPOINT}/users/leaderboard", json=payload)
    assert create_response.status_code == HTTPStatus.OK
    assert isinstance(create_response.json()["leaderboard"], list)


def test_leaderboard_graph():
    payload = {"type": "graph"}
    create_response = requests.get(f"{ENDPOINT}/users/leaderboard", json=payload)
    assert create_response.status_code == HTTPStatus.OK
    assert create_response.text == '<img src="/static/graph.png">'
