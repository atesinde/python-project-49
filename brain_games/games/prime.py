import random

from brain_games.utility.is_num_simple import is_num_simple


def prime_game():
    message_question = (''
        'Answer "yes" if given number is prime. '
        'Otherwise answer "no".'
    )
    question = random.randint(2, 100)
    if is_num_simple(question):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return message_question, question, right_answer