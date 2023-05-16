from random import randint
import prompt

def greet():
    print('Welcome to the Brain Games!')

def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

def get_question_answer():
    num = randint(1, 100)
    if num % 2 == 0:
        answer = 'yes'
    if num % 2 != 0:
        answer = 'false'
    return str(num), question


def play_even():
    greet()
    name = welcome_user()
    count = 0
    while true:
        question, answer = get_question_answer()
        print(f"Question: {random_num}")
        play_answer = prompt.string("Your answer: ")
        if play_answer == 'yes':
            count += 1
        if play_answer == 'false':
            break
            print("""'yes' is wrong answer ;(. Correct answer was 'no'.""")
        if count == 3:
            print('congrats')
