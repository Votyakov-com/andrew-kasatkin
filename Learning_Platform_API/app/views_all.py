from app import app, models
from flask import request, Response
from http import HTTPStatus

List_of_Users = models.User.USERS
List_of_Expressions = models.Expression.EXPRS
List_of_Questions = models.Question.QUEST


@app.route("/")
def index():
    response = (
        f"<h1>All statistics</h1><br>"
        f"<h3>---Users---</h3>{'<br>'.join([user.repr() for user in List_of_Users])}<br><br>"
        f"<h3>---Expressions---</h3><br>{'<br>'.join([expr.repr() for expr in List_of_Expressions])}<br><br>"
        f"<h3>---Questions---</h3><br>{'<br>'.join([quest.repr() for quest in List_of_Questions])}<br><br>"
    )
    return response


@app.route("/save_data")
def save_data():
    choice = request.get_json()["save_progress"]
    if choice == "TRUE" or "true":
        models.User.save_users(List_of_Users)
        models.Expression.save_expressions(List_of_Expressions)
        models.Question.save_questions(List_of_Questions)
        response = Response(response="Your data has been saved!", status=HTTPStatus.OK)
    else:
        response = Response(response="Bad request!", status=HTTPStatus.BAD_REQUEST)
    return response
