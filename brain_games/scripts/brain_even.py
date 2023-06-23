from random import randint
import prompt


def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def get_question_answer():
    num = randint(1, 100)
    if num % 2 == 0:
        answer = 'yes'
    if num % 2 != 0:
        answer = 'no'
    return str(num), answer


def play_even():
    greet()
    name = welcome_user()
    print("""Answer "yes" if the number is even, otherwise answer "no".""")
    count_correct_answer = 0
    while True:
        question, answer = get_question_answer()
        print(f"Question: {question}")
        play_answer = prompt.string("Your answer: ")
        if answer == play_answer:
            count_correct_answer += 1
        if answer != play_answer:
            print(f"""'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!""")
            break
        elif count_correct_answer == 3:
            print(f"Congratulations, {name}")
            break
