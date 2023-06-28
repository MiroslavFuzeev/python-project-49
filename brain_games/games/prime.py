from random import randint
from math import sqrt
import prompt


RULES = '''Answer "yes" if given number is prime. Otherwise answer "no".'''

limit_1 = 1
limit_2 = 100

def get_question_answer():
    question = randint(limit_1, limit_2)
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
    return question, answer

