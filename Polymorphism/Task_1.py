from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(self):
        raise NotImplementedError('Error! Wrong value.')

class Autobiography(Book):
    def display(self):
        print(f'"{self.title}" - прекрасная книга, написанная в автобиографическом жанре. Автор - {self.author}')

class Psychology(Book):
    def display(self):
        print(f'"{self.title}" - прекрасная книга, написанная в жанре психологии. Автор - {self.author}')


class Fantasy(Book):
    def display(self):
        print(f'"{self.title}" - прекрасная книга, написанная в в жанре фэнтези. Автор - {self.author}')



