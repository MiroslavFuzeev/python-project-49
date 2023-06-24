from random import randint


def get_question_answer():
    num = randint(1, 100)
    if num % 2 == 0:
        answer = 'yes'
    if num % 2 != 0:
        answer = 'no'
    return str(num), answer


RULES = """Answer "yes" if the number is even, otherwise answer "no"."""
