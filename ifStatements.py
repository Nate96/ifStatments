import random

class ifStatements():

    @staticmethod
    def _is_even(number):
        return number % 2 == 0

    @staticmethod
    def _is_greater_than_ten(number):
        return number > 10

    @staticmethod
    def _is_smaller(target, number):
        return number < target

    @staticmethod
    def _get_range_hint(symbol):
        return symbol == 'r' or symbol == 'R'

    @staticmethod
    def _get_even_or_odd_hint(symbol):
        return symbol == "e" or symbol == "E"

    @staticmethod
    def _give_instructions():
        print()

    @staticmethod
    def _is_lower(input, target):
        return input < target

    def _getting_hints(self, hint_symbol, target):
        if self._get_range_hint(hint_symbol):
            if self._is_greater_than_ten(target):
                print("The number is larger than 10")
            else:
                print("The number is smaller than 10")
            return False

        if self._get_even_or_odd_hint(hint_symbol):
            if self._is_even(target):
                print("The number is even")
            else:
                print("The number is odd")
            return False
        return True

    def _guessing_numbers(self, attempt, target):
        if attempt == target:
            print("Nailed it!!")
        elif self._is_lower(attempt, target):
            print("higher")
        else:
            print("lower")

    def run(self):
        self._give_instructions()

        target = random.randint(1, 21)
        attempt = raw_input("Guess a number: ")

        while attempt != -1:
            if self._getting_hints(str(attempt), target):
                self._guessing_numbers(int(attempt), int(target))
            attempt = raw_input("Guess a number: ")


if __name__ == "__main__":
    game = ifStatements()
    game.run()