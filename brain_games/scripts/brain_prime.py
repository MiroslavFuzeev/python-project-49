from random import randint
from math import sqrt
import prompt

def greet():
    print('Welcome to the Brain Games!')
  
def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name

def get_question_answer():
    question = randint(1, 100)
    prime = True
    i = 2
    while i <= sqrt(question):
        if question % i == 0:
            prime = False
            break
        i += 1
    if prime:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
  
def play_prime():
    greet()
    name = welcome_user()
    print ('''Answer "yes" if given number is prime. Otherwise answer "no".''')
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

