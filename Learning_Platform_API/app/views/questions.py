from app import app, models
from flask import request, Response
import json
from http import HTTPStatus
import random

List_of_Users = models.User.USERS
List_of_Questions = models.Question.QUEST


@app.post("/question/create")  # Создание вопроса - любого
def question_creation():
    data = request.get_json()
    title = data["title"]
    description = data["description"]
    question_type = data["type"]
    quest_id = len(List_of_Questions)
    question = None
    if question_type == "ONE-ANSWER":
        answer = data["answer"]  # expect string
        if not models.OneAnswerQuestion.is_valid(answer):
            return Response(status=HTTPStatus.BAD_REQUEST)
        question = models.OneAnswerQuestion(
            quest_id, title, description, answer, reward=1
        )
        response = Response(
            json.dumps(
                {
                    "id": quest_id,
                    "title": title,
                    "description": description,
                    "type": question_type,
                    "answer": answer,
                }
            ),
            HTTPStatus.OK,
            mimetype="application/json",
        )

    elif question_type == "MULTIPLE-CHOICE":
        choices = data["choices"]  # it`s list
        answer = data["answer"]  # expect number
        if not models.MultipleChoiceQuestion.is_valid(answer, choices):
            return Response(
                "Answer must be int, choices must be list.",
                status=HTTPStatus.BAD_REQUEST,
            )
        question = models.MultipleChoiceQuestion(
            quest_id, title, description, answer, choices, reward=1
        )
        response = Response(
            json.dumps(
                {
                    "id": quest_id,
                    "title": title,
                    "description": description,
                    "type": question_type,
                    "choices": choices,
                    "answer": answer,
                }
            ),
            HTTPStatus.OK,
            mimetype="application/json",
        )
    if question is None:
        response = Response("Bad type of question", status=HTTPStatus.BAD_REQUEST)
    List_of_Questions.append(question)
    return response


@app.get("/question/random")
def get_random_question():

    if len(List_of_Questions) == 0:
        return Response(response="Add some questions!", status=HTTPStatus.NOT_FOUND)
    question = random.choice(List_of_Questions)
    question_id = List_of_Questions.index(question)
    response = Response(
        json.dumps(
            {
                "question_id": question_id,
                "reward": question.reward,
            }
        ),
        HTTPStatus.OK,
        mimetype="application/json",
    )
    return response


@app.post("/questions/<int:question_id>/solve")
def question_solve(question_id):
    data = request.get_json()
    user_id = data["user_id"]

    if models.User.is_user_valid(user_id):
        return Response(response="Bad value of user!", status=HTTPStatus.BAD_REQUEST)
    if models.Question.is_quest_valid(question_id):
        return Response(
            response="Bad value of question!", status=HTTPStatus.BAD_REQUEST
        )

    user_answer = data["user_answer"]
    question = List_of_Questions[question_id]
    user = List_of_Users[user_id]

    if isinstance(question, models.MultipleChoiceQuestion):
        if not isinstance(user_answer, int):
            return Response(response="Bad type of value", status=HTTPStatus.BAD_REQUEST)
    if isinstance(question, models.OneAnswerQuestion):
        if not isinstance(user_answer, str):
            return Response(response="Bad type of value", status=HTTPStatus.BAD_REQUEST)

    sign = False
    for item in range(len(user.history)):
        if question.title == user.history[item]["title"]:
            result = "You can`t answer one question twice!"
            reward = 0
            sign = True

    if sign is False:
        if user_answer == question.answer:
            user.score_increase(question.reward)
            result = "CORRECT"
            reward = question.reward
        else:
            result = "INCORRECT"
            reward = 0
        user.question_to_history(question, user_answer)
    response = Response(
        json.dumps(
            {
                "question_id": question_id,
                "result": result,
                "reward": reward,
            }
        ),
        HTTPStatus.OK,
        mimetype="application/json",
    )
    return response
