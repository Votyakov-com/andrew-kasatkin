from http import HTTPStatus
import requests
from app.tests.test_users import correct_user_payload

ENDPOINT = "http://127.0.0.1:5000"


def create_one_answer_question():
    return {
        "title": "Test one-answer question",
        "description": "question",
        "type": "ONE-ANSWER",
        "answer": "splendor",
    }


def create_multiple_choice_question():
    return {
        "title": "Test multiple-choice question",
        "description": "question",
        "type": "MULTIPLE-CHOICE",
        "choices": ["squalor", "dwindle", "enhance"],
        "answer": 2,
    }


def test_question_creating():
    # Работа с вопросом с одним вариантом ответа
    payload_1 = create_one_answer_question()
    response_1 = requests.post(f"{ENDPOINT}/question/create", json=payload_1)
    assert response_1.status_code == HTTPStatus.OK
    data_1 = response_1.json()
    assert data_1["title"] == payload_1["title"]
    assert data_1["description"] == payload_1["description"]
    assert data_1["type"] == payload_1["type"]
    assert data_1["answer"] == payload_1["answer"]

    # Работа с вопросом с вариантом выбора ответа
    payload_2 = create_multiple_choice_question()
    response_2 = requests.post(f"{ENDPOINT}/question/create", json=payload_2)
    assert response_2.status_code == HTTPStatus.OK
    data_2 = response_2.json()
    assert data_2["title"] == payload_2["title"]
    assert data_2["description"] == payload_2["description"]
    assert data_2["type"] == payload_2["type"]
    assert data_2["answer"] == payload_2["answer"]
    assert data_2["choices"] == payload_2["choices"]


def test_random_questions():
    # Создание и проверка создания вопросов
    quantity = 5
    list_of_id = list()
    for _ in range(quantity):
        payload = create_one_answer_question()
        response = requests.post(f"{ENDPOINT}/question/create", json=payload)
        assert response.status_code == HTTPStatus.OK
        list_of_id.append(response.json()["id"])
        payload = create_multiple_choice_question()
        response = requests.post(f"{ENDPOINT}/question/create", json=payload)
        assert response.status_code == HTTPStatus.OK
        list_of_id.append(response.json()["id"])

    # Отправка запроса на случайный вопрос и его проверка
    response_4 = requests.get(f"{ENDPOINT}/question/random")
    assert response_4.status_code == HTTPStatus.OK
    assert response_4.json()["question_id"] in range(0, max(list_of_id))


def test_question_solve():
    # Создание user`a который будет отвечать на вопрос
    user_payload = correct_user_payload()
    user_response = requests.post(f"{ENDPOINT}/users/create", json=user_payload)
    assert user_response.status_code == HTTPStatus.CREATED
    user_id = user_response.json()["id"]

    # Создание вопроса для верного ответа
    quest_payload_1 = create_multiple_choice_question()
    quest_response_1 = requests.post(
        f"{ENDPOINT}/question/create", json=quest_payload_1
    )
    assert quest_response_1.status_code == HTTPStatus.OK
    question_id_1 = quest_response_1.json()["id"]
    expression_answer_1 = quest_payload_1["answer"]

    # Создание вопроса для неверного ответа
    quest_payload_2 = create_one_answer_question()
    quest_response_2 = requests.post(
        f"{ENDPOINT}/question/create", json=quest_payload_2
    )
    assert quest_response_2.status_code == HTTPStatus.OK
    question_id_2 = quest_response_2.json()["id"]
    expression_answer_2 = quest_payload_2["answer"]

    # Отправка user`ом верного ответа на вопрос
    payload_1 = {
        "user_id": user_id,
        "user_answer": expression_answer_1,
    }
    solve_response_1 = requests.post(
        f"{ENDPOINT}/questions/{question_id_1}/solve", json=payload_1
    )
    assert solve_response_1.status_code == HTTPStatus.OK
    assert solve_response_1.json()["question_id"] == question_id_1
    assert solve_response_1.json()["result"] == "CORRECT"

    # Отправка user`ом неверного ответа на вопрос
    payload_2 = {
        "user_id": user_id,
        "user_answer": expression_answer_2,
    }
    wrong_solve_response_2 = requests.post(
        f"{ENDPOINT}/questions/{question_id_2}/solve", json=payload_2
    )
    assert wrong_solve_response_2.status_code == HTTPStatus.OK
    assert wrong_solve_response_2.json()["question_id"] == question_id_2
    assert wrong_solve_response_2.json()["result"] == "CORRECT"
