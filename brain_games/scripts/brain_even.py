from brain_games.cli import welcome_user
import random
import prompt

def main():
    print('Welcome to the Brain Games!')
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
        if user_answer == right_answer:
            print('Correct!')
            rounds_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{right_answer}'.\nLet's try again, {user_name}!")
            break
    if rounds_count == 3:
        print(f'Congratulations, {user_name}!')

if __name__ == "__main__":
    main()