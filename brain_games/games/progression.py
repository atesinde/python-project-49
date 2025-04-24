import random


def progression_game():
    message_question = 'What number is missing in the progression?'
    progression_start = random.randint(0, 20)
    progression_add = random.randint(0, 5)
    progression_length = random.randint(5, 15)
    progression_element = progression_start
    progression = []
    for i in range(progression_length):
        progression.append(progression_element)
        progression_element += progression_add
    right_answer = random.choice(progression)
    missed_element_index = progression.index(right_answer)
    progression[missed_element_index] = '..'
    question = f"{' '.join(map(str, progression))}"
    return message_question, question, right_answer