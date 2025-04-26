import random


def is_num_prime(number):
    for i in range(2, number // 2):
        if number % i == 0:
            return False
    return True


def prime_game():
    message_question = (''
        'Answer "yes" if given number is prime. '
        'Otherwise answer "no".'
    )
    question = random.randint(2, 100)
    if is_num_prime(question):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return message_question, question, right_answer