from random import randint


RULES = '''Answer "yes" if given number is prime. Otherwise answer "no".'''


LIMIT_1 = 1
LIMIT_2 = 100


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def get_question_answer():
    question = randint(LIMIT_1, LIMIT_2)
    prime = is_prime(question)
    answer = 'yes' if prime else 'no'
    return str(question), answer
