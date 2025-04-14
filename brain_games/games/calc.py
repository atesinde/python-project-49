import random

import prompt

from brain_games.engine import is_answer_right


def calc_game(user_name):
    print('What is the result of the expression?')
    rounds_count = 0
    operations = ['+', '-', '*']
    while rounds_count < 3:
        generated_number1 = random.randint(1, 100)
        generated_number2 = random.randint(1, 100)
        generated_operation = random.choice(operations)
        print(f'Question: {generated_number1} {generated_operation} {generated_number2}')
        match generated_operation:
            case '+':
                right_answer = generated_number1 + generated_number2
            case '-':
                right_answer = generated_number1 - generated_number2
            case '*':
                right_answer = generated_number1 * generated_number2
        user_answer = prompt.integer('Your answer: ')
        if not is_answer_right(user_name, user_answer, right_answer):
            break
        else:
            rounds_count += 1
    if rounds_count == 3:
        print(f'Congratulations, {user_name}!')