from random import randint


RULES = """Answer "yes" if the number is even, otherwise answer "no"."""

LIMIT_1 = 1
LIMIT_2 = 100

def get_question_answer():
    num = randint(LIMIT_1, LIMIT_2)
    if num % 2 == 0:
        answer = 'yes'
    if num % 2 != 0:
        answer = 'no'
    return str(num), answer



