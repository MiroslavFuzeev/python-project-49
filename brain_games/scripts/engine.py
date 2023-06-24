#!/usr/bin/env python3

from random import randint
from random import choice
import prompt


def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def run_game(rules, func_get_question_answer):
    greet()
    name = welcome_user()
    count_correct_answer = 0
    print(rules)
    while True:
      question, answer = func_get_question_answer()
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

