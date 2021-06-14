import unittest
from unittest.mock import patch
from game_pc_guess_num import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        """Создаем игру и начальные параметры"""
        self.game = Game()
        self.game.number_list = [0, 1, 2]
        self.game.try_count = 0

    @patch('builtins.input', return_value='no')
    def test_is_win_false(self, mock_input):
        """ПК не угадал число"""
        self.assertFalse(self.game.is_win(0))

    @patch('builtins.input', return_value='y')
    def test_is_win_trur(self, mock_input):
        """ПК угадал число"""
        self.assertTrue(self.game.is_win(0))

    def test_get_number(self):
        """ПК выбирает целое число из списка"""
        self.assertIsNotNone(self.game.get_number())
        self.game.get_number()
        self.game.get_number()
        self.assertIsNone(self.game.get_number())


if __name__ == '__main__':
    unittest.main()
