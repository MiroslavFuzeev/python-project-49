
from brain_games.scripts.engine import run_game
from brain_games.games.gcd import get_question_answer, RULES

def main():
     run_game(rules=RULES, func_get_question_answer=get_question_answer)


if __name__ == "__main__":
    main()
