from random import randint
from random import choice
import prompt
import math

def get_question_answer():
    num = randint(1, 100)
    intrval = randint(1,10)
    list_len = randint(5,10)
    num2 = num + intrval*list_len
    mylist = range(num, num2, intrval)
    question = [i for i in mylist]
    answer = choice(question)
    answer_index = question.index(answer)
    question[answer_index] = '..'
    return question, answer

RULES = "What number is missing in the progression?"