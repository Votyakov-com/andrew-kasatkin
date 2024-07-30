import Task_1


def main():
    Machine1 = Task_1.CoffeeMachine(40, 20, 15, 30, 15)
    Machine1.add_milk(12)
    Machine1.add_cups(2)

    cups_amount = int(input('How many cups of coffee do you want to order: '))
    water = int(input('How much water do you want to have in your beverage (in mil.): '))
    coffe = int(input('How much pure coffee do you want to have in your beverage (in mil.): '))
    milk = int(input('How much milk do you want to have in your beverage (in mil.): '))
    sugar = int(input('How much sugar do you want to have in your beverage (in gr.): '))
    print('---------')
    print(' Pending ')
    print('---------')
    Customer = Machine1.make_coffee(water * cups_amount, coffe * cups_amount, milk * cups_amount,
                                    sugar * cups_amount, cups_amount)


main()
