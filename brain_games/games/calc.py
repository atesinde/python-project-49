import random


def calc_game():
    message_question = 'What is the result of the expression?'
    operations = ['+', '-', '*']
    generated_number1 = random.randint(1, 100)
    generated_number2 = random.randint(1, 100)
    generated_operation = random.choice(operations)
    question = f'{generated_number1} {generated_operation} {generated_number2}'
    match generated_operation:
        case '+':
            right_answer = generated_number1 + generated_number2
        case '-':
            right_answer = generated_number1 - generated_number2
        case '*':
            right_answer = generated_number1 * generated_number2
    return message_question, question, right_answer