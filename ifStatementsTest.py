import unittest
from ifStatements import ifStatements


class TestIfStatement(unittest.TestCase):
    def setUp(self):
        self.ifStatements = ifStatements()

    def test_isEvent(self):
        self.assertTrue(self.ifStatements._is_even(2))
        self.assertTrue(self.ifStatements._is_even(-4))

        self.assertFalse(self.ifStatements._is_even(5))
        self.assertFalse(self.ifStatements._is_even(-7))

    def test_is_greater_than_ten(self):
        self.assertTrue(self.ifStatements._is_greater_than_ten(13))

        self.assertFalse(self.ifStatements._is_greater_than_ten(10))

        self.assertFalse(self.ifStatements._is_greater_than_ten(3))

    def test_is_smaller(self):
        self.ifStatements.target_number = 5

        self.assertFalse(self.ifStatements._is_smaller(6))

        self.assertTrue(self.ifStatements._is_smaller(4))

    def test_get_range_hint(self):
        self.assertTrue(self.ifStatements._get_range_hint('r'))
        self.assertTrue(self.ifStatements._get_range_hint('R'))

        self.assertFalse(self.ifStatements._get_range_hint('h'))
        self.assertFalse(self.ifStatements._get_range_hint('H'))

    def test_getting_hints(self):
        self.ifStatements._getting_hints('r', 15)
        self.ifStatements._getting_hints('r', 5)

        self.ifStatements._getting_hints('e', 15)
        self.ifStatements._getting_hints('e', 4)

        self.ifStatements._getting_hints(1, 15)

    def test_get_even_or_odd_hint(self):
        self.assertTrue(self.ifStatements._get_even_or_odd_hint('o'))
        self.assertTrue(self.ifStatements._get_even_or_odd_hint('O'))

        self.assertFalse(self.ifStatements._get_even_or_odd_hint('h'))
        self.assertFalse(self.ifStatements._get_even_or_odd_hint('H'))

    def test_guessing_number(self):
        self.ifStatements._guessing_numbers(5, 6)

        self.ifStatements._guessing_numbers(10, 5)

        self.ifStatements._guessing_numbers(1, 1)

        self.ifStatements._guessing_numbers('r', 3)

