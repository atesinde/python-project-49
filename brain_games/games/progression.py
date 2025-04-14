import random

import prompt

from brain_games.engine import is_answer_right


def progression_game(user_name):
    print('What number is missing in the progression?')
    rounds_count = 0
    while rounds_count < 3:
        progression_start = random.randint(0, 20)
        progression_add = random.randint(0, 5)
        progression_length = random.randint(5, 15)
        progression_element = progression_start
        progression = []
        for i in range(progression_length):
            progression.append(progression_element)
            progression_element += progression_add
        right_answer = random.choice(progression)
        missed_element_index = progression.index(right_answer)
        progression[missed_element_index] = '..'
        print(f'Question: {' '.join(map(str, progression))}')
        user_answer = prompt.integer('Your answer: ')
        if not is_answer_right(user_name, user_answer, right_answer):
            break
        else:
            rounds_count += 1
    if rounds_count == 3:
        print(f'Congratulations, {user_name}!')