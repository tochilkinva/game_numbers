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


if __name__ == '__main__':
    game = Game()
    game.start()
