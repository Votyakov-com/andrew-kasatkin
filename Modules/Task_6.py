import math

a = int(input('Number1: '))
b = int(input('Number2: '))
c = int(input('Number3: '))

answer1 = False
answer2 = False

if a == 0:
    if b == 0:
        raise ValueError('Data is wrong!')
    else:
        answer1 = -c / b
elif b == 0:
    if a >= 0:
        raise ValueError('Data is wrong!')
    else:
        answer1 = math.sqrt(c / a)
elif c == 0:
    if a == 0:
        raise ValueError('Data is wrong!')
    else:
        answer1 = -b / a
else:
    answer1 = (b - math.sqrt(b ^ 2 + 4 * a * c) / 2 * a)
    answer2 = (b + math.sqrt(b ^ 2 + 4 * a * c) / 2 * a)

if answer2 is False:
    print(f'This equation has only one decision: {answer1:,.2f}')
else:
    print(f'This equation has two decisions: {answer1:,.2f},{answer2:,.2f}')
