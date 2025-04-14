def is_answer_right(user_name, user_answer, right_answer, rounds_count):
        if user_answer == right_answer:
            print('Correct!')
            return True
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{right_answer}'.\nLet's try again, {user_name}!")
            return False