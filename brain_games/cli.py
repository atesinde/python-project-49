import prompt


def welcome_user():
    name = prompt.string('May I have your name, newcomer? ')
    print(f'Hello, {name}!')
    return name