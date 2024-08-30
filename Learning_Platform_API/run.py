from app import app, models


def load_progress():
    USERS_archive = models.User.load_users()
    EXPRESSIONS_archive = models.Expression.load_expressions()
    QUESTIONS_archive = models.Question.load_questions()
    for item in USERS_archive:
        models.User.USERS.append(item)
    for item in EXPRESSIONS_archive:
        models.Expression.EXPRS.append(item)
    for item in QUESTIONS_archive:
        models.Question.QUEST.append(item)


if __name__ == "__main__":
    load_progress()
    app.run()
