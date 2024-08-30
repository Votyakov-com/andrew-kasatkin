import Task_10_calculator as calc

ADD = 1
SUBTRACT = 2
MULTIPLY = 3
DIVIDE = 4
QUIT = 5


def main():
    choice = 0
    while choice != QUIT:
        result = None

        choice, number1, number2 = menu()
        if choice == ADD:
            result = calc.add(number1, number2)
        elif choice == SUBTRACT:
            result = calc.subtract(number1, number2)
        elif choice == MULTIPLY:
            result = calc.multiply(number1, number2)
        elif choice == DIVIDE:
            result = calc.divide(number1, number2)

        if result is not None:
            print(f'Your result is {result:,.2f}')

    print('See you soon!')


def menu():
    number1 = None
    number2 = None

    print()
    print('Menu:')
    print('"1" - Add two numbers')
    print('"2" - Subtract one number from another')
    print('"3" - Multiply two numbers')
    print('"4" - Divide one number to another')
    print('"5" - Quit the program')
    print()
    choice = int(input('Enter your choice: '))
    print()
    if ADD <= choice <= QUIT:
        if choice == QUIT:
            pass
        else:
            number1 = int(input("Enter your first number: "))
            number2 = int(input("Enter your second number: "))
    else:
        raise ValueError('Error! Wrong data')

    return choice, number1, number2


if __name__ == "__main__":
    main()
