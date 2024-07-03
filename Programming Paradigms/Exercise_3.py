def sum_even_numbers(numbers):
    list_of_even_numbers = list()
    for item in numbers:
        if item % 2 == 0:
            list_of_even_numbers.append(item)
    return sum(list_of_even_numbers)


Numbers = [60, 84, 9, 49, 7, 85, 38]
print('The total of even numbers in list is: ', sum_even_numbers(Numbers))
