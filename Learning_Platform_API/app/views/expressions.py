from app import app, models
from flask import request, Response
import json
from http import HTTPStatus
import random

List_of_Users = models.User.USERS
List_of_Expressions = models.Expression.EXPRS


@app.get("/math/expression")  # Поступает json c данными, которые превращаются в пример
def generate_expression():
    data = request.get_json()
    expr_id = len(List_of_Expressions)
    count_nums = data["count_nums"]
    operation = data["operation"]  # expect +,-,*,//,**

    if operation == "random":
        operation = random.choice(["+", "-", "*", "//", "**"])

    if count_nums <= 1 or (count_nums > 2 and operation in ("-", "**", "//")):
        return Response(
            response="Rewrite your math expression!", status=HTTPStatus.BAD_REQUEST
        )

    min_number = data["min"]
    max_number = data["max"]

    values = [random.randint(min_number, max_number) for _ in range(count_nums)]
    expression = models.Expression(expr_id, operation, *values)
    List_of_Expressions.append(expression)

    response = Response(
        json.dumps(
            {
                "id": expression.ex_id,
                "operation": expression.operation,
                "values": expression.values,
                "string_expression": expression.transform_to_string(),
            }
        ),
        HTTPStatus.OK,
        mimetype="application/json",
    )
    return response


@app.get("/math/<int:exp_id>")
def get_expression(exp_id):  # Отправка пользователю мат.примера
    if models.Expression.is_expr_valid(exp_id):
        return Response(
            response="Bad value of expression!", status=HTTPStatus.BAD_REQUEST
        )
    expression_from_storage = List_of_Expressions[exp_id]
    response = Response(
        json.dumps(
            {
                "id": expression_from_storage.ex_id,
                "operation": expression_from_storage.operation,
                "values": expression_from_storage.values,
                "string_expression": expression_from_storage.transform_to_string(),
            }
        ),
        HTTPStatus.OK,
        mimetype="application/json",
    )
    return response


@app.post("/math/<int:exp_id>/solve")  # Сюда приходит решение в виде JSON
def expression_solve(exp_id):
    data = request.get_json()
    user_id = data["user_id"]

    if models.User.is_user_valid(user_id):
        return Response(response="Bad value of user!", status=HTTPStatus.BAD_REQUEST)
    if models.Expression.is_expr_valid(exp_id):
        return Response(
            response="Bad value of expression!", status=HTTPStatus.BAD_REQUEST
        )

    user_answer = data["user_answer"]
    if user_answer == List_of_Expressions[exp_id].answer:

        List_of_Users[user_id].score_increase(List_of_Expressions[exp_id].reward)
        result = "CORRECT"
        reward = List_of_Expressions[exp_id].reward
    else:
        result = "INCORRECT"
        reward = 0

    response = Response(
        json.dumps(
            {
                "expression_id": exp_id,
                "result": result,
                "reward": reward,
            }
        ),
        HTTPStatus.OK,
        mimetype="application/json",
    )
    return response
