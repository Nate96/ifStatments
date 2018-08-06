import random


def _is_even(number):
    return number % 2 == 0


def _is_greater_than_ten(guessed_number):
    return guessed_number > 10


def _is_smaller(guessed_number, random_number):
    return guessed_number < random_number


def _get_range_hint(symbol):
    return symbol == 'r' or symbol == 'R'


def _get_even_or_odd_hint(symbol):
    return symbol == 'o' or symbol == 'O'


def _if_exit(symbol):
    return symbol == 'e' or symbol == 'E'


def _give_instructions():
    print()


def _is_lower(guessed_compare, random_number):
    return guessed_compare < random_number


def _getting_hints(hint_symbol, number):
    if _get_range_hint(hint_symbol):
        if _is_greater_than_ten(number):
            print("The number is larger than 10")
        else:
            print("The number is smaller than 10")
        return False

    if _get_even_or_odd_hint(hint_symbol):
        if _is_even(number):
            print("The number is even")
        else:
            print("The number is odd")
        return False
    return True


def _guessing_numbers(guessed_number, random_number):
    if guessed_number == random_number:
        print("Nailed it!!")
    elif _is_lower(guessed_number, random_number):
        print("higher")
    else:
        print("lower")


if __name__ == "__main__":
    _give_instructions()

    target = random.randint(1, 21)
    attempt = raw_input("Guess a number: ")

    while not _if_exit(str(attempt)):
        if _getting_hints(str(attempt), target):
            _guessing_numbers(int(attempt), target)
        attempt = raw_input("Guess a number: ")