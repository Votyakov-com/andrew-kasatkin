from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def vote_command(self):
        pass

    @abstractmethod
    def gesture_command(self):
        pass


class Lock(ABC):
    @abstractmethod
    def close_lock(self):
        pass

    @abstractmethod
    def open_lock(self):
        pass


class SmartAssistant(Command):
    def vote_command(self):
        print('Умный помощник распознал голосовую команду')

    def gesture_command(self):
        print('Умный помощник распознал жестовые команды')


class SmartCamera(Command, Lock):
    def vote_command(self):
        print('Умная камера распознала голосовую команду')

    def gesture_command(self):
        print('Умная камера распознала жестовые команды')

    def close_lock(self):
        print('Умная камера закрыла замок входной двери')

    def open_lock(self):
        print('Умная камера открыла замок входной двери')


class SmartLock(Lock):
    def close_lock(self):
        print('Умный замок закрыл входную дверь')

    def open_lock(self):
        print('Умный замок открыл входную дверь')


sa = SmartAssistant()
sa.vote_command()
sa.gesture_command()
print()
sc = SmartCamera()
sc.open_lock()
sc.close_lock()
sc.vote_command()
sc.gesture_command()
print()
sl = SmartLock()
sl.open_lock()
sl.close_lock()
