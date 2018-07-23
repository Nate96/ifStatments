import unittest
import ifStatements


class TestIfStatement(unittest.TestCase):

    def test_isEvent(self):
        self.assertTrue(ifStatements._is_even(2))
        self.assertTrue(ifStatements._is_even(-4))

        self.assertFalse(ifStatements._is_even(5))
        self.assertFalse(ifStatements._is_even(-7))

    def test_is_greater_than_ten(self):
        self.assertTrue(ifStatements._is_greater_than_ten(13))

        self.assertFalse(ifStatements._is_greater_than_ten(10))

        self.assertFalse(ifStatements._is_greater_than_ten(3))

    def test_is_smaller(self):
        self.assertFalse(ifStatements._is_smaller(6, 10))

        self.assertTrue(ifStatements._is_smaller(4, 3))

    def test_get_range_hint(self):
        self.assertTrue(ifStatements._get_range_hint('r'))
        self.assertTrue(ifStatements._get_range_hint('R'))

        self.assertFalse(ifStatements._get_range_hint('h'))
        self.assertFalse(ifStatements._get_range_hint('H'))

    def test_getting_hints(self):
        ifStatements._getting_hints('r', 15)
        ifStatements._getting_hints('R', 5)

        ifStatements._getting_hints('o', 15)
        ifStatements._getting_hints('O', 4)

        ifStatements._getting_hints(1, 15)

    def test_get_even_or_odd_hint(self):
        self.assertTrue(ifStatements._get_even_or_odd_hint('o'))
        self.assertTrue(ifStatements._get_even_or_odd_hint('O'))

        self.assertFalse(ifStatements._get_even_or_odd_hint('h'))
        self.assertFalse(ifStatements._get_even_or_odd_hint('H'))

    def test_guessing_number(self):
        ifStatements._guessing_numbers(5, 6)

        ifStatements._guessing_numbers(10, 5)

        ifStatements._guessing_numbers(1, 1)

        ifStatements._guessing_numbers('r', 3)

