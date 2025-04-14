import random

import prompt

from brain_games.engine import is_answer_right
from brain_games.utility.is_num_simple import is_num_simple


def prime_game(user_name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    rounds_count = 0
    while rounds_count < 3:
        number = random.randint(2, 100)
        if is_num_simple(number):
            right_answer = 'yes'
        else:
            right_answer = 'no'
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ')
        if not is_answer_right(user_name, user_answer, right_answer):
            break
        else:
            rounds_count += 1
    if rounds_count == 3:
        print(f'Congratulations, {user_name}!')