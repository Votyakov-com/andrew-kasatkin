class Animal():
    def __init__(self, name):
        self.name = name

    def feed(self):
        print(f'Feeding the {self.name} bread crumbs')


def feed(obj):
    obj.feed()


feed(Animal('swan'))
feed(Animal('duck'))
feed(Animal('mouse'))

# Программа не соответствовала принципу DRY - Don`t Repeat Yourself
