from random import randint
from math import sqrt
import prompt

def get_question_answer():
    question = randint(1, 100)
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

RULES = '''Answer "yes" if given number is prime. Otherwise answer "no".'''