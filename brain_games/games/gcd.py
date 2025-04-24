import math

import random


def gcd_game():
    message_question = 'Find the greatest common divisor of given numbers.'
    generated_number1 = random.randint(1, 100)
    generated_number2 = random.randint(1, 100)
    question = f'{generated_number1} {generated_number2}'
    right_answer = math.gcd(generated_number1, generated_number2)
    return message_question, question, right_answer