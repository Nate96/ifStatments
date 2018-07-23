import random


def _is_even(number):
    return number % 2 == 0


def _is_greater_than_ten(number):
    return number > 10


def _is_smaller(target, attempt):
    return attempt < target


def _get_range_hint(symbol):
    return symbol == 'r' or symbol == 'R'


def _get_even_or_odd_hint(symbol):
    return symbol == 'o' or symbol == 'O'


def _give_instructions():
    print()


def _is_lower(attempt, target):
    return attempt < target


def _getting_hints(hint_symbol, target):
    if _get_range_hint(hint_symbol):
        if _is_greater_than_ten(target):
            print("The number is larger than 10")
        else:
            print("The number is smaller than 10")
        return False

    if _get_even_or_odd_hint(hint_symbol):
        if _is_even(target):
            print("The number is even")
        else:
            print("The number is odd")
        return False
    return True


def _guessing_numbers(attempt, target):
    if attempt == target:
        print("Nailed it!!")
    elif _is_lower(attempt, target):
        print("higher")
    else:
        print("lower")


def run(self):
    _give_instructions()

    target = random.randint(1, 21)
    attempt = raw_input("Guess a number: ")

    while attempt != 'e' or attempt != 'E':
        if self._getting_hints(str(attempt), target):
            self._guessing_numbers(int(attempt), target)
        attempt = raw_input("Guess a number: ")


if __name__ == "__main__":
    _give_instructions()

    target = random.randint(1, 21)
    attempt = raw_input("Guess a number: ")

    while attempt != 'e' or attempt != 'E':
        if _getting_hints(str(attempt), target):
            _guessing_numbers(int(attempt), target)
        attempt = raw_input("Guess a number: ")