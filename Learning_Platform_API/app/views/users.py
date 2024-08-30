from app import app, models
from flask import request, Response, url_for
import json
from http import HTTPStatus
import matplotlib.pyplot as plt

List_of_Users = models.User.USERS


@app.post("/users/create")  # Приходит json с данными
def user_creating():
    data = request.get_json()
    first_name = data["first_name"]
    last_name = data["last_name"]
    phone = data["phone"]
    email = data["email"]
    user_id = len(List_of_Users)

    if models.User.is_phone_valid(phone) is not True:
        return Response(response="Bad user`s phone!", status=HTTPStatus.BAD_REQUEST)

    if not models.User.is_email_valid(email):
        return Response(response="Bad user`s email!", status=HTTPStatus.BAD_REQUEST)

    user = models.User(first_name, last_name, phone, email, user_id)
    List_of_Users.append(user)
    response = Response(
        json.dumps(
            {
                "id": user.user_id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "phone": user.phone,
                "email": user.email,
                "score": user.score,
            }
        ),
        HTTPStatus.CREATED,
        mimetype="application/json",
    )
    return response


@app.get("/users/<int:user_id>")  # Происходит проброс переменной
def user_check(user_id):
    if models.User.is_user_valid(user_id):
        return Response(response="Bad value of user!", status=HTTPStatus.NOT_FOUND)
    user = List_of_Users[user_id]
    response = Response(
        json.dumps(
            {
                "id": user.user_id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "phone": user.phone,
                "email": user.email,
                "score": user.score,
            }
        ),
        HTTPStatus.OK,
        mimetype="application/json",
    )
    return response


@app.get("/users/<int:user_id>/history")
def get_user_history(user_id):
    if models.User.is_user_valid(user_id):
        return Response(response="Bad value of user!", status=HTTPStatus.NOT_FOUND)

    response = Response(
        json.dumps({"history": List_of_Users[user_id].history}),
        HTTPStatus.OK,
        mimetype="application/json",
    )
    return response


@app.get("/users/leaderboard")
def get_leaderboard():
    data = request.get_json()
    data_type = data["type"]

    if data_type == "table":
        leaderboard = [
            user.convert_to_dict() for user in sorted(List_of_Users, reverse=True)
        ]
        response = Response(
            json.dumps({"leaderboard": leaderboard}),
            HTTPStatus.OK,
            mimetype="application/json",
        )

    elif data_type == "graph":
        users_names = [f"{user.first_name} {user.last_name}" for user in List_of_Users]
        users_levels = [user.score for user in List_of_Users]

        plt.bar(
            users_names,
            users_levels,
            color=[
                "red" if users_levels[i] == max(users_levels) else "blue"
                for i in range(len(users_names))
            ],
        )
        plt.ylabel("Users scores")
        plt.xlabel("Users names")

        plt.savefig("app/static/graph.png")

        response = Response(
            response=f'<img src="{url_for('static',filename='graph.png')}">',
            status=HTTPStatus.OK,
            mimetype="text/html",
        )

    else:
        response = Response("Bad type value", status=HTTPStatus.BAD_REQUEST)

    return response
