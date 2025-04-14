from brain_games.engine import is_answer_right
import random
import prompt
import math


def gcd_game(user_name):
    print('Find the greatest common divisor of given numbers.')
    rounds_count = 0
    while rounds_count < 3:
        generated_number1 = random.randint(1,100)
        generated_number2 = random.randint(1,100)
        print(f'Question: {generated_number1} {generated_number2}')
        right_answer = math.gcd(generated_number1, generated_number2)
        user_answer = prompt.integer('Your answer: ')
        if not is_answer_right(user_name, user_answer, right_answer):
            break
        else:
            rounds_count += 1
    if rounds_count == 3:
        print(f'Congratulations, {user_name}!')