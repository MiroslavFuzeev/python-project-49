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
    num2 = randint(1, 100)
    question = num, num2
    answer = math.gcd(num, num2)
    return question, answer


def play_gcd():
    greet()
    name = welcome_user()
    print ("Find the greatest common divisor of given numbers.")
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

