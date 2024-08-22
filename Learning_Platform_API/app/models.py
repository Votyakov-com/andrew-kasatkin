import json
import re
from abc import ABC, abstractmethod
import pickle


class User:
    USERS = list()  # objects of class User

    def __init__(self, first_name, last_name, phone, email, user_id, score=0):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.user_id = user_id
        self.score = score
        self.history = list()

    @staticmethod
    def is_email_valid(email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)

    @staticmethod
    def is_phone_valid(phone):
        match = re.search(
            re.compile(r"(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}"),
            phone,
        )
        if match:
            return True
        return False

    def score_increase(self, amount=1):
        self.score += amount

    @staticmethod
    def is_user_valid(user_id):
        return user_id < 0 or user_id >= len(User.USERS)

    def repr(self):
        return f"id {self.user_id} - " f" {self.first_name}" f" {self.last_name}"

    def question_to_history(self, question, user_answer):
        data = {
            "title": question.title,
            "description": question.description,
            "type": question.quest_type,
            "answer": question.answer,
            "user_answer": user_answer,
            "reward": question.reward if user_answer == question.answer else 0,
        }
        self.history.append(data)

    def __lt__(self, other):
        return self.score < other.score

    def convert_to_dict(self):
        return dict(
            {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "score": self.score,
            }
        )

    @staticmethod
    def load_users():
        try:
            with open("app/static/USERS.txt", "rb") as file1:
                USERS = pickle.load(file1)
        except IOError:
            USERS = list()
        return USERS

    @staticmethod
    def save_users(data_to_save):
        with open("app/static/USERS.txt", "wb") as file1:
            pickle.dump(data_to_save, file1)


class Expression:
    EXPRS = list()  # objects of class Expression

    def __init__(self, ex_id, operation, *values, reward=None):
        self.ex_id = ex_id
        self.operation = operation
        self.values = values
        self.answer = self.__evaluate()
        if reward is None:
            reward = len(values) - 1  # reward for right solution of expression
        self.reward = reward

    def __evaluate(self):
        return eval(self.transform_to_string())

    def transform_to_string(self):
        expression_string = str(self.values[0])
        for value in self.values[1:]:
            expression_string = (
                expression_string + " " + self.operation + " " + str(value)
            )
        return expression_string

    @staticmethod
    def is_expr_valid(expr_id):
        return expr_id < 0 or expr_id >= len(Expression.EXPRS)

    def repr(self):
        return (
            f"ID: {self.ex_id}\n "
            f"Expression: {self.transform_to_string()}\n "
            f"Answer: {self.answer}"
        )

    @staticmethod
    def load_expressions():
        try:
            with open("app/static/EXPRESSIONS.txt", "rb") as file1:
                EXPRS = pickle.load(file1)
        except IOError:
            EXPRS = list()
        return EXPRS

    @staticmethod
    def save_expressions(data_to_save):
        with open("app/static/EXPRESSIONS.txt", "wb") as file1:
            pickle.dump(data_to_save, file1)


class Question(ABC):
    QUEST = list()  # objects of class Question

    def __init__(self, question_id, title, description, reward=None):
        self.quest_id = question_id
        self.title = title
        self.description = description
        self.reward = reward
        if reward is None:
            reward = 1  # reward for right solution of question
        self.reward = reward

    @property
    @abstractmethod
    def answer(self): ...

    def repr(self):
        return f"ID: {self.quest_id}  Title: {self.title}"

    @staticmethod
    def is_quest_valid(quest_id):
        return quest_id < 0 or quest_id >= len(Question.QUEST)

    @staticmethod
    def load_questions():
        try:
            with open("app/static/QUESTIONS.txt", "rb") as file1:
                QUEST = pickle.load(file1)
        except IOError:
            QUEST = list()
        return QUEST

    @staticmethod
    def save_questions(data_to_save):
        with open("app/static/QUESTIONS.txt", "wb") as file1:
            pickle.dump(data_to_save, file1)


class OneAnswerQuestion(Question):
    def __init__(self, question_id, title, description, answer: str, reward=None):
        super().__init__(question_id, title, description, reward)
        self._answer = answer
        self.quest_type = "ONE-ANSWER"

    @property
    def answer(self):
        return self._answer

    @answer.setter
    def answer(self, value: str):
        self._answer = value

    @staticmethod
    def is_valid(answer):
        return isinstance(answer, str)


class MultipleChoiceQuestion(Question):
    def __init__(
        self, question_id, title, description, answer: int, choices=list, reward=None
    ):
        super().__init__(question_id, title, description, reward)
        self.choices = choices
        self._answer = answer
        self.quest_type = "MULTIPLE-CHOICE"

    @property
    def answer(self):
        return self._answer

    @answer.setter
    def answer(self, value: int):
        self._answer = value

    @staticmethod
    def is_valid(answer, choices):
        if not isinstance(answer, int) or not isinstance(choices, list):
            return False
        if answer < 0 or answer >= len(choices):
            return False
        return True
