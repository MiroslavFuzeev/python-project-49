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

name = welcome_user()

def get_question_answer():
  random_num = randint(1, 100)
  print(f"Question: {random_num}")
  answ = prompt.string("Your answer: ")
  if random_num % 2 == 0:
    if answ == 'yes':
      print("Correct!")
    if answ == 'no':
      print("""'no' is wrong answer ;(. Correct answer was 'yes'.""")
      print(f"Let's try again, {name}!")
  if random_num % 2 != 0:
    if answ == 'no':
      print("Correct!")
    if answ == 'yes':
      print("""'yes' is wrong answer ;(. Correct answer was 'no'.""")
      print(f"Let's try again, {name}!")


count = 0
while count < 3:
  get_question_answer()
  count += 1
print((f"Congratulations, {name}!"))
