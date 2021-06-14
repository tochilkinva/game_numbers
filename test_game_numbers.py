import unittest
from unittest.mock import patch
from game_guess_num import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        """Создаем игру и начальные параметры"""
        self.game = Game()
        self.game.number_range = 50
        self.game.win_num = 30
        self.game.try_count = 0

    def test_is_win(self):
        """Игра позволяет выиграть"""
        self.assertTrue(self.game.is_win(30))
        self.assertFalse(self.game.is_win(0))
        self.assertFalse(self.game.is_win(100))

    def test_hint(self):
        """Игра дает подсказки"""
        self.assertEqual(self.game.hint(10),
                         'Подсказка: число должно быть намного больше')
        self.assertEqual(self.game.hint(50),
                         'Подсказка: число должно быть намного меньше')
        self.assertEqual(self.game.hint(25),
                         'Подсказка: число должно быть чуть больше')
        self.assertEqual(self.game.hint(35),
                         'Подсказка: число должно быть чуть меньше')

    @patch('builtins.input', return_value=10)
    def test_get_number_int(self, mock_input):
        """Игрок вводит целое число"""
        num = self.game.get_number()
        self.assertEqual(num, 10)

    @patch('builtins.input', return_value='no')
    def test_get_number_str(self, mock_input):
        """Игрок вводит не целое число и получает None"""
        num = self.game.get_number()
        self.assertIsNone(num)


if __name__ == '__main__':
    unittest.main()
