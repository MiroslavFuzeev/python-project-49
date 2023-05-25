from random import randint
from random import choice
import prompt

def greet():
    print('Welcome to the Brain Games!')
  

def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name

#Функция задает вопрос
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

def play_calc():
    greet()
    name = welcome_user()
    print ("What is the result of the expression?")
    count_correct_answer = 0
    while True:
      question, answer = get_question_answer()
      print(f'Question: {question}')
      user_answer = prompt.string('Your answer: ')
      if user_answer == str(answer):
        print('Correct!')
        count_correct_answer += 1
      if user_answer != str(answer):
        print(f"'{user_answer}' is wrong answer ;(."
          f"Correct answer was '{answer}'.\n"
          f"Let's try again, {name}!")
        exit()
      elif count_correct_answer == 3:
        print(f"Congratulations, {name}")
        break
