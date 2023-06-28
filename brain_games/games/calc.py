from random import randint
from random import choice
import prompt

RULES = "What is the result of the expression?"

limit_1 = 1
limit_2 = 100

def get_question_answer():
    num = randint(limit_1, limit_2)
    num2 = randint(limit_1, limit_2)
    simb_list = ['+', '-' , '*']
    rand_simb_list = choice(simb_list)
    question = str(num) + rand_simb_list + str(num2)
    if rand_simb_list == '+':
      answer = num + num2
    if rand_simb_list == '-':
      answer = num - num2
    if rand_simb_list == '*':
      answer = num * num2
    return  question, answer
