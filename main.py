import random

num = random.randint(1, 10)


def number_check_function():
    if guess == num:
        print('Абсолютно верно!')
    elif guess > 10:
        print('Номер больше 10')
    elif guess < 1:
        print('Номер меньше 1')
    else:
        print('Неугадали, число было ' + str(num))


guess = int(input('Угадайте число от 1 до 10:'))

number_check_function()