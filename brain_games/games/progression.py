from random import randint

notice = 'What number is missing in the progression?'

progression_length = 10

min_number = 1
max_number = 10

progression_start = randint(min_number, max_number)
progression_step = randint(min_number, max_number)


def make_progression(start, step, length):
    progression = [start]
    i = 1
    while i <= length:
        progression.append(progression[i - 1] + step)
        i += 1

    return progression


question_position = randint(min_number, max_number)
make_question = make_progression(
    progression_start, progression_step, progression_length
)

answer = make_question[question_position]
make_question[question_position] = '..'
question = ' '.join(map(str, make_question))
