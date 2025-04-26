import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name, newcomer? ')
    print(f'Hello, {name}!')
    return name


def is_answer_right(user_name, user_answer, right_answer):
    if user_answer == right_answer:
        print('Correct!')
        return True
    else:
        print(
            f"'{user_answer}' is wrong answer ;(. " 
            f"Correct answer was '{right_answer}'.\n"
            f"Let's try again, {user_name}!"
        )
        return False

    
def game_engine(game):
    user_name = welcome_user()
    rounds_count = 3
    game_message, _, _ = game()
    print(game_message)
    for i in range(rounds_count):
        _, question, right_answer = game()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if not is_answer_right(user_name, user_answer, right_answer):
            return
        if i == rounds_count - 1:
            print(f'Congratulations, {user_name}!')