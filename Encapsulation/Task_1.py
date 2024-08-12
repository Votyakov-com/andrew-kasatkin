from random import *


class CRM:
    def __init__(self):
        self.__students = dict()

    def add(self, abiturient):
        number = abiturient.get_number()  # получение СНИЛСа абитуриента
        if number in self.__students:
            raise ValueError('This applicant is already in archive!')
        self.__students[number] = abiturient  # Добавление абитуриента

    def get_status(self, number):
        return self.__students[number].get_check()


class Abiturient:
    def __init__(self, name, surname, patronymic, age, number, bvi=False):
        self.__name = name
        self.__surname = surname
        self.__patronymic = patronymic
        self.__age = age
        self.__number = number  # СНИЛС
        self.__RNE = self.__fetch_RNE()  # Баллы RNE
        self.__bvi = bvi

    def get_number(self):  # Отправка приватного атрибута 'СНИЛС' в другой класс
        return self.__number

    def get_check(self):  # Отправка приватного метода
        return self.__check()

    def __fetch_RNE(self):  # Получение баллов за RNE
        return tuple(randint(0, 100) for _ in range(3))

    def __check(self):  # Проверка на проход
        if self.__bvi:
            return "Да"
        if random() > 0.95:
            return "Да"
        return "Нет"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise ValueError('Your data is wrong')

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if isinstance(surname, str):
            self.__surname = surname
        else:
            raise ValueError('Your data is wrong')

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, patronymic):
        if isinstance(patronymic, str):
            self.__patronymic = patronymic
        else:
            raise ValueError('Your data is wrong')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if isinstance(age, int) and 17 < age < 99:
            self.__age = age
        else:
            raise ValueError('Your data is wrong')

    @property
    def bvi(self):
        return self.__bvi

    @bvi.setter
    def bvi(self, bvi):
        if isinstance(bvi, bool):
            self.__bvi = bvi
        else:
            raise ValueError('Your data is wrong')

    @property
    def RNE(self):
        return self.__RNE

    @RNE.setter
    def RNE(self, RNE):
        if isinstance(RNE, tuple) and len(list((n for n in RNE if 50 if 50 < n <= 100))) == 3:
            self.__RNE = RNE
        else:
            raise ValueError('Your data is wrong')


module = CRM()
s1 = Abiturient("Александр", "Вотяков", "Романович", 18, "111-222-333 00", True)
s2 = Abiturient("Роман", "Вотяков", "Александрович", 18, "333-222-111 00")
module.add(s1)
module.add(s2)
print(module.get_status("111-222-333 00"))
print(module.get_status("333-222-111 00"))
