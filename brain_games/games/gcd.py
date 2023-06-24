#!/usr/bin/env python3
from random import randint
import math


def get_question_answer():
    num = randint(1, 100)
    num2 = randint(1, 100)
    question = num, num2
    answer = math.gcd(num, num2)
    return question, answer

RULES = "Find the greatest common divisor of given numbers."
