# Hi there!
## You can play 5 games here: 
#### brain-even
_The essence of the game is this: the user is shown a random number. And he needs to answer yes if the number is even, or no if the number is odd._
#### brain-calc
_The essence of the game is the following: the user is shown a random mathematical expression, for example, 35 + 16, which is to calculate and write the correct answer._
#### brain-gcd
_The essence of the game is this: the user is shown two random numbers, for example 25 50. The user must calculate and enter the greatest common divisor of these numbers._
#### brain-progression
_The essence of the game is this: We show the player a series of numbers that form an arithmetic progression, replacing any of the numbers with two points. The player must determine this number._
#### brain-prime
_The essence of the game is this: Answer "yes" if given number is prime. Otherwise answer "no"._

### Hexlet tests and linter status:
[![Actions Status](https://github.com/MiroslavFuzeev/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/MiroslavFuzeev/python-project-49/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/7b7be59841192f8d8bec/maintainability)](https://codeclimate.com/github/MiroslavFuzeev/python-project-49/maintainability)

### About The Project Installation Usage
_To install the package, use the following commands:_
1. git clone 
2. make build publish package-install
3. enjoy

_To add game:_ 
1. add file ....py to "games" directory. Must contain only game logic (get_question_answer() and constants)
2. add file brain_....py to "scripts" directory. Must contain only game logic (main())
3. make import settings following the examples 
4. add new dependency into pyproject.toml section: \[tool.poetry.scripts\]
5. delite dist/ directory
6. make build publish package-install

### Watch how to play the games: 
[Asciinema_brain_even](https://asciinema.org/a/5bTU5bZmuf8fbYlyqktx9emoN)

[Asciinema_brain_calc](https://asciinema.org/a/HiMZtYnkrRm8oXNOh2TgzFI01)

[Asciinema_brain_gcd](https://asciinema.org/a/BwTjZXknkf92Em4eSNBYNWn03)

[Asciinema_brain_progression](https://asciinema.org/a/JEuKpNMzCbXY2kJFlkc3xgOCy)

[Asciinema_brain_prime](https://asciinema.org/a/i1BBQtweLZ71e46HZM6vmtmkS)