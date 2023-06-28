from random import randint


RULES = """Answer "yes" if the number is even, otherwise answer "no"."""

limit_1 = 1
limit_2 = 100

def get_question_answer():
    num = randint(limit_1, limit_2)
    if num % 2 == 0:
        answer = 'yes'
    if num % 2 != 0:
        answer = 'no'
    return str(num), answer



