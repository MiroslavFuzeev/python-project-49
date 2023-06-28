from random import randint
from random import choice
import prompt
import math


RULES = "What number is missing in the progression?"

limit_1 = 1
limit_2 = 100

int_lim_1 = 1
int_lim_2 = 10

list_len_lim_1 = 5
list_len_lim_2 = 10


def get_question_answer():
    num = randint(limit_1, limit_2)
    intrval = randint(int_lim_1, int_lim_2)
    list_len = randint(list_len_lim_1, list_len_lim_2)
    num2 = num + intrval*list_len
    mylist = range(num, num2, intrval)
    question = [i for i in mylist]
    answer = choice(question)
    answer_index = question.index(answer)
    question[answer_index] = '..'
    return question, answer
