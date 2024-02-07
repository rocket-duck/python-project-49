from random import randint

notice = 'Answer "yes" if given number is prime. Otherwise answer "no".'

min_number = 1
max_number = 100


def is_prime(number):
    if number < 2:
        return False

    i = 2
    while i <= number / 2:
        if number % i == 0:
            return False
        i += 1

    return True


question = randint(min_number, max_number)
answer = 'yes' if is_prime(question) else 'no'
