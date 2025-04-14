from brain_games.cli import welcome_user
from brain_games.games_common_operations import is_answer_right
import random
import prompt

def main():
    user_name = welcome_user()
    print('What is the result of the expression?')
    rounds_count = 0
    operations = ['+', '-', '*']
    while rounds_count < 3:
        generated_number1 = random.randint(1,100)
        generated_number2 = random.randint(1,100)
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
        if not is_answer_right(user_name, user_answer, right_answer, rounds_count):
            break
        else:
            rounds_count += 1
    if rounds_count == 3:
        print(f'Congratulations, {user_name}!')

if __name__ == "__main__":
    main()