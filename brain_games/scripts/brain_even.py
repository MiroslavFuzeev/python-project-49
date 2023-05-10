from random import randint
import prompt

def greet():
    print('Welcome to the Brain Games!')

greet()


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name

welcome_user()


print("""Answer "yes" if the number is even, otherwise answer "no".""")

def is_even ():
  random_num = randint(1, 100)
  print(f"Question: {random_num}")
  answ = prompt.string("Your answer: ")
  count = 0
  if random_num % 2 == 0:
    if answ == 'yes':
      count += 1
      print("Correct!")
      is_even ()
    if answ == 'no':
      print("""'no' is wrong answer ;(. Correct answer was 'yes'.""")
      print(f"Let's try again, {name}!")
  if random_num % 2 != 0:
    if answ == 'no':
      count += 1
      print("Correct!")
      is_even ()
    if answ == 'yes':
      print("""'yes' is wrong answer ;(. Correct answer was 'no'.""")
      print(f"Let's try again, {name}!")
  for i in range(3):
    if count == 3:
      print("Congratulations, Bill!")


is_even ()