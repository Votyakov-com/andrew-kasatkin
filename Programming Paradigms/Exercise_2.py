def sum_even_numbers(numbers):
    return sum(filter(lambda number: number%2==0, numbers))

numbers = [14, 93, 19, 38, 18, 51, 77]
print('The total of even numbers in list is: ',sum_even_numbers(numbers))