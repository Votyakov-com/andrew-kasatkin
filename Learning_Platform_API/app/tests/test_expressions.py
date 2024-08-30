from http import HTTPStatus
import requests
import random
from app.tests.test_users import correct_user_payload

ENDPOINT = "http://127.0.0.1:5000"


def correct_payload():
    return {
        "count_nums": 2,
        "operation": random.choice(["+", "-", "*", "//", "**"]),
        "min": random.randint(1, 10),
        "max": random.randint(12, 21),
    }


def test_generate_expression():
    payload = correct_payload()

    # Получение ответа от POST запроса
    create_response = requests.get(f"{ENDPOINT}/math/expression", json=payload)
    # Тест на верный статус ответа
    assert create_response.status_code == HTTPStatus.OK
    # Распаковка JSON ответа
    expression_data = create_response.json()
    expression_id = expression_data["id"]

    # Сверка данных из первоначальной отправки и вернувшегося
    assert expression_data["operation"] == payload["operation"]
    for value in expression_data["values"]:
        assert payload["min"] <= value <= payload["max"]

    # Получение ответа от GET запроса на проверку существования
    create_response_2 = requests.get(f"{ENDPOINT}/math/{expression_id}")

    # Сверка данных из первоначальной отправки и вернувшегося
    assert create_response_2.json()["id"] == expression_id
    assert create_response_2.json()["operation"] == payload["operation"]
    for value in expression_data["values"]:
        assert payload["min"] <= value <= payload["max"]


def test_expression_create_with_wrong_data():
    payload_with_wrong_operation = {
        "count_nums": 3,
        "operation": "**",
        "min": random.randint(1, 10),
        "max": random.randint(12, 21),
    }
    payload_with_wrong_nums = {
        "count_nums": 1,
        "operation": random.choice(["+", "-", "*", "//", "**"]),
        "min": random.randint(1, 10),
        "max": random.randint(2, 20),
    }

    create_response_with_wrong_operation = requests.get(
        f"{ENDPOINT}/math/expression", json=payload_with_wrong_operation
    )

    create_response_with_wrong_nums = requests.get(
        f"{ENDPOINT}/math/expression", json=payload_with_wrong_nums
    )

    assert create_response_with_wrong_operation.status_code == HTTPStatus.BAD_REQUEST
    assert create_response_with_wrong_nums.status_code == HTTPStatus.BAD_REQUEST


def test_correct_question_solve():
    # Создание мат.вопроса
    expr_payload = correct_payload()
    expr_response = requests.get(f"{ENDPOINT}/math/expression", json=expr_payload)
    assert expr_response.status_code == HTTPStatus.OK
    expression_id = expr_response.json()["id"]
    expression_str = expr_response.json()["string_expression"]

    # Создание user`a который будет мат.вопрос решать
    user_payload = correct_user_payload()
    user_response = requests.post(f"{ENDPOINT}/users/create", json=user_payload)
    assert user_response.status_code == HTTPStatus.CREATED
    user_id = user_response.json()["id"]

    # Отправка решения мат.примера пользователем
    payload = {
        "user_id": user_id,
        "user_answer": eval(expression_str),
    }
    solve_response = requests.post(
        f"{ENDPOINT}/math/{expression_id}/solve", json=payload
    )
    assert solve_response.status_code == HTTPStatus.OK
    assert solve_response.json()["expression_id"] == expression_id
    assert solve_response.json()["result"] == "CORRECT"


def test_question_solve():
    # Создание мат.вопроса
    expr_payload = correct_payload()
    expr_response = requests.get(f"{ENDPOINT}/math/expression", json=expr_payload)
    assert expr_response.status_code == HTTPStatus.OK
    expression_id = expr_response.json()["id"]
    expression_str = expr_response.json()["string_expression"]

    # Создание user`a который будет мат.вопрос решать
    user_payload = correct_user_payload()
    user_response = requests.post(f"{ENDPOINT}/users/create", json=user_payload)
    assert user_response.status_code == HTTPStatus.CREATED
    user_id = user_response.json()["id"]

    # Отправка верного решения мат.примера пользователем
    payload = {
        "user_id": user_id,
        "user_answer": eval(expression_str),
    }
    solve_response = requests.post(
        f"{ENDPOINT}/math/{expression_id}/solve", json=payload
    )
    assert solve_response.status_code == HTTPStatus.OK
    assert solve_response.json()["expression_id"] == expression_id
    assert solve_response.json()["result"] == "CORRECT"

    # Отправка ложного решения мат.примера пользователем
    payload_2 = {
        "user_id": user_id,
        "user_answer": eval(expression_str) + random.randint(1, 100),
    }
    solve_response_2 = requests.post(
        f"{ENDPOINT}/math/{expression_id}/solve", json=payload_2
    )
    assert solve_response_2.status_code == HTTPStatus.OK
    assert solve_response_2.json()["expression_id"] == expression_id
    assert solve_response_2.json()["result"] == "INCORRECT"
