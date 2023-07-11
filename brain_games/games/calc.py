from random import randint
from random import choice


RULES = "What is the result of the expression?"


LIMIT_1 = 1
LIMIT_2 = 100


def calculate_answer(num, num2, rand_simb_list):
    if rand_simb_list == ' + ':
        answer = num + num2
        return answer
    if rand_simb_list == ' - ':
        answer = num - num2
        return answer
    if rand_simb_list == ' * ':
        answer = num * num2
        return answer


def get_question_answer():
    num = randint(LIMIT_1, LIMIT_2)
    num2 = randint(LIMIT_1, LIMIT_2)
    simb_list = [' + ', ' - ', ' * ']
    rand_simb_list = choice(simb_list)
    question = str(num) + rand_simb_list + str(num2)
    answer = calculate_answer(num, num2, rand_simb_list)
    return question, str(answer)
