from random import randint
from random import choice
import prompt
import math


RULES = "What number is missing in the progression?"

LIMIT_1 = 1
LIMIT_2 = 100

INT_LIM_1 = 1
INT_LIM_2 = 10

LIST_LEN_LIM_1 = 5
LIST_LEN_LIM_2 = 10


def get_question_answer():
    num = randint(LIMIT_1, LIMIT_2)
    intrval = randint(INT_LIM_1, INT_LIM_2)
    list_len = randint(LIST_LEN_LIM_1, LIST_LEN_LIM_2)
    num2 = num + intrval*list_len
    mylist = range(num, num2, intrval)
    question = [i for i in mylist]
    answer = choice(question)
    answer_index = question.index(answer)
    question[answer_index] = '..'
    return question, answer
