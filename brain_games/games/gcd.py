#!/usr/bin/env python3
from random import randint
import math


RULES = "Find the greatest common divisor of given numbers."

limit_1 = 1
limit_2 = 100

def get_question_answer():
    num = randint(limit_1, limit_2)
    num2 = randint(limit_1, limit_2)
    question = num, num2
    answer = math.gcd(num, num2)
    return question, answer


