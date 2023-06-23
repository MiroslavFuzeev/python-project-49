#!/usr/bin/env python3

from engine import run_game
from games.calc import get_answer_question, RULES

def main():
     run_game(RULES, get_answer_question)


if __name__ == "__main__":
    main()

