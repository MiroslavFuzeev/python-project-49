#!/usr/bin/env python3
from random import randint
import math


RULES = "Find the greatest common divisor of given numbers."

LIMIT_1 = 1
LIMIT_2 = 100

def get_question_answer():
    num = randint(LIMIT_1, LIMIT_2)
    num2 = randint(LIMIT_1, LIMIT_2)
    question = num, num2
    answer = math.gcd(num, num2)
    return question, answer


