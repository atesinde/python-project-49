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
    rounds_count = 0
    game_message, _, _ = game()
    print(game_message)
    while rounds_count < 3:
        _, question, right_answer = game()
        print(f'Question: {question}')
        if type(right_answer) is str:
            user_answer = prompt.string('Your answer: ')
        else:
            user_answer = prompt.integer('Your answer: ')
        if not is_answer_right(user_name, user_answer, right_answer):
            break
        else:
            rounds_count += 1
    if rounds_count == 3:
        print(f'Congratulations, {user_name}!')