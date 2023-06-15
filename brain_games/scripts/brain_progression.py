from random import randint
from random import choice
import prompt
import math

def greet():
    print('Welcome to the Brain Games!')
  

def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name

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


def play_progression():
    greet()
    name = welcome_user()
    print ("What number is missing in the progression?")
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
        break
      elif count_correct_answer == 3:
        print(f"Congratulations, {name}")
        break

