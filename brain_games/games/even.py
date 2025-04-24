import random


def even_game():
    message_question = (
        'Answer "yes" if the number is even, '
        'otherwise answer "no".'
    )
    question = random.randint(1, 100)
    if question % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return message_question, question, right_answer
