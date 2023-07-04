#!/usr/bin/env python3


from brain_games.engine import run_game
from brain_games.games.prime import get_question_answer, RULES


def main():
    run_game(rules=RULES, func_get_question_answer=get_question_answer)


if __name__ == "__main__":
    main()
