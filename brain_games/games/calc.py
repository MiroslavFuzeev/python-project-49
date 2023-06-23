from random import randint
from random import choice
import prompt


def get_question_answer():
    simb_list = ['+', '-' , '*']
    num = randint(1, 100)
    num2 = randint(1, 100)
    rand_simb_list = choice(simb_list)
    question = str(num) + rand_simb_list + str(num2)
    if rand_simb_list == '+':
      answer = num + num2
    if rand_simb_list == '-':
      answer = num - num2
    if rand_simb_list == '*':
      answer = num * num2
    return  question, answer

RULES = "What is the result of the expression?"

