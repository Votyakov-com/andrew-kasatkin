from abc import ABC, abstractmethod


class Human(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def answer_question(self, question=None):
        print('Очень интересный вопрос! Давайте разбираться вместе!')


class Student(Human):
    @staticmethod
    def ask_question(human, question):
        print(f'{human.name}, {question}')
        human.answer_question(question)
        print()

    def answer_question(self, question=None):
        print('Я ещё не умею!')


class Teacher(Human):
    def answer_question(self, question=None):
        if question == 'как войти в айти?':
            print('Можешь начать осваивать программирование с ППШ')
        elif question == 'как научится программировать?':
            print('Сейчас расскажу')
        else:
            super().answer_question()


class Mentor(Human):
    def answer_question(self, question=None):
        if question == 'как повысить эффективность работы?':
            print('Важно соблюдать три правила')
        else:
            super().answer_question()


class Curator(Human):
    def answer_question(self, question=None):
        if question == 'как додуматься до этого решения?':
            print('Проверил. Замечательный вариант решения. Вы отлично справились!')
        else:
            super().answer_question()


class CodeReviewer(Human):
    def answer_question(self, question=None):
        if question == 'я усовершенствовал свой код. Вы проверите?':
            print('Сейчас опишу ход мыслей при решении задачи')
        else:
            super().answer_question()


student1 = Student('Ваня')
teacher = Teacher('Александр Романович')
mentor1 = Mentor('Илья')
curator1 = Curator('Владимир')
reviewer1 = CodeReviewer('Евгений')

student1.ask_question(teacher, 'как войти в айти?')
student1.ask_question(teacher, 'как научится программировать?')
student1.ask_question(mentor1, 'как повысить эффективность работы?')
student1.ask_question(curator1, 'как додуматься до этого решения?')
student1.ask_question(reviewer1, 'я усовершенствовал свой код. Вы проверите?')
student1.ask_question(reviewer1, 'когда проверите pull-request`ы?')
