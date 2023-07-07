from random import randint
from math import sqrt


RULES = '''Answer "yes" if given number is prime. Otherwise answer "no".'''


LIMIT_1 = 1
LIMIT_2 = 100


def get_question_answer():
    question = randint(LIMIT_1, LIMIT_2)
    prime = True
    i = 2
    while i <= sqrt(question):
        if question % i == 0:
            prime = False
            break
        i += 1
    if prime:
        answer = 'yes'
    else:
        answer = 'no'
    return str(question), answer
