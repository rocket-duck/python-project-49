from random import randint

notice = 'Find the greatest common divisor of given numbers.'

min_number = 1
max_number = 20

number_1 = randint(min_number, max_number)
number_2 = randint(min_number, max_number)


def find_GCD(num_1, num_2):
    if num_2 > num_1:
        return find_GCD(num_2, num_1)

    if num_2 == 0:
        return num_1

    return find_GCD(num_2, num_1 % num_2)


question = f'{number_1} {number_2}'
answer = find_GCD(number_1, number_2)
