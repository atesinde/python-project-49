import random

import prompt

from brain_games.engine import is_answer_right


def even_game(user_name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    rounds_count = 0
    while rounds_count < 3:
        generated_number = random.randint(1, 100)
        print(f'Question: {generated_number}')
        if generated_number % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'
        user_answer = prompt.string('Your answer: ')
        if not is_answer_right(user_name, user_answer, right_answer):
            break
        else:
            rounds_count += 1
    if rounds_count == 3:
        print(f'Congratulations, {user_name}!')