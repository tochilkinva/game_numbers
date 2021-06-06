# Алгоритм игры
# создаем список чисел
# случайно загадываем число
# просим ввести число
#     проверка это число или нет
#     угадали
#     неугадали
#         жарко холодно
# Вы угадали число за н попыток

import random
import unittest

MIN_NUMBER = 10
MAX_NUMBER = 100


class Game():
    """Игра угадай целое число"""

    def __init__(self):
        """Инициализация параметров"""
        self.number_range = random.randint(MIN_NUMBER, MAX_NUMBER)
        self.win_num = random.randint(0, self.number_range)
        self.try_count = 0
        # print('win_num = ', self.win_num) # Число для победы

    def start(self):
        """Запуск игры"""
        print('---------------------------------------------')
        print(f'Угадайте целое число от 0 до {self.number_range}!')
        print('---------------------------------------------')
        while True:
            num = self.get_number()
            if num is None:
                continue

            if self.is_win(num):
                self.end_game()
                break

    def get_number(self):
        """Ввод целого числа и проверка"""
        try:
            print()
            num = int(input('Введите число: '))
            self.try_count += 1
        except ValueError:
            print('Это не число, попробуйте снова.')
            return None
        else:
            return num

    def is_win(self, num):
        """Проверка условия победы"""
        if num not in range(self.number_range + 1):
            print()
            print(f'Нужно ввести число от 0 до {self.number_range}')
            return False

        if num != self.win_num:
            print('Не угадали, попробуйте еще.')
            print(self.hint(num))
            return False

        return True

    def hint(self, num):
        """Подсказка для игрока"""
        if abs(num - self.win_num) > 6:
            ampl = 'намного'
        else:
            ampl = 'чуть'
        if num > self.win_num:
            return f'Подсказка: число должно быть {ampl} меньше'
        else:
            return f'Подсказка: число должно быть {ampl} больше'

    def end_game(self):
        """Это конец игры"""
        print('----------------------------------------------')
        print((f'Поздравляем! Вы угадали число {self.win_num}'
               f' за {self.try_count} попыток!'))
        print('----------------------------------------------')


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

        self.game.number_range = 50
        self.game.win_num = 30
        self.game.try_count = 0

    def test_is_win(self):
        self.assertTrue(self.game.is_win(30))
        self.assertFalse(self.game.is_win(0))
        self.assertFalse(self.game.is_win(100))

    def test_hint(self):
        self.assertEqual(self.game.hint(10),
                         'Подсказка: число должно быть намного больше')
        self.assertEqual(self.game.hint(50),
                         'Подсказка: число должно быть намного меньше')
        self.assertEqual(self.game.hint(25),
                         'Подсказка: число должно быть чуть больше')
        self.assertEqual(self.game.hint(35),
                         'Подсказка: число должно быть чуть меньше')

    def test_get_number(self):
        # self.assertEqual(self.game.is_win(5), '22')
        pass


if __name__ == '__main__':
    # Закомментировать для игры
    # unittest.main()

    game = Game()
    game.start()
