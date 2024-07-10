def partial_apply(func, argument1):
    def partial_func(argument2):
        return func(argument1, argument2)

    return partial_func


function = lambda number1, number2: number1 * number2

multiplier_for_5 = partial_apply(function, 5)

number_to_multiply_for_5 = int(input("What number do you want to multiply for 5: "))

print(multiplier_for_5(number_to_multiply_for_5))
