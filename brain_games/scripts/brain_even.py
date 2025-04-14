from brain_games.cli import welcome_user
from brain_games.games_common_operations import is_answer_right
import random
import prompt

def main():
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    rounds_count = 0
    while rounds_count < 3:
        generated_number = random.randint(1,100)
        print(f'Question: {generated_number}')
        if generated_number % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'
        user_answer = prompt.string('Your answer: ')
        if not is_answer_right(user_name, user_answer, right_answer, rounds_count):
            break
        else:
            rounds_count += 1
    if rounds_count == 3:
        print(f'Congratulations, {user_name}!')

if __name__ == "__main__":
    main()