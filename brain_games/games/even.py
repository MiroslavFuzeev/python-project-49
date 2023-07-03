from random import randint


RULES = """Answer "yes" if the number is even, otherwise answer "no"."""

LIMIT_1 = 1
LIMIT_2 = 100

def is_even():
    if num % 2 == 0:
        return True
    if num % 2 != 0:
        return False

def get_question_answer():
    num = randint(LIMIT_1, LIMIT_2)
    answer = is_even()
    answer = 'yes' if answer else 'no'
    return str(num), answer
    



