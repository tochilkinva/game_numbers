# Алгоритм игры
# создаем список чисел
# Человек загадывает число
# ПК пытается угадать число
#     проверка это то число или нет
#       угадали
#       неугадали
#         жарко холодно
# ПК угадал число за н попыток
# ПК перепробовал все чилслаб вы обманули ПК?

import time
import random

MAX_NUMBER = 10


class Game():
    """Игра ПК угадывает целое число"""

    def __init__(self):
        """Инициализация параметров"""
        self.try_count = 0
        self.number_list = [num for num in range(MAX_NUMBER + 1)]

    def start(self):
        """Запуск игры"""
        print('---------------------------------------------')
        print(f'Загадайте целое число от 0 до {MAX_NUMBER}!')
        print('---------------------------------------------')
        while True:
            num = self.get_number()
            if num is None:
                self.cheat()
                break

            if self.is_win(num):
                self.end_game(num)
                break

    def get_number(self):
        """Получение целого числа из списка self.number_list"""
        self.try_count += 1
        if len(self.number_list) > 0:
            return self.number_list.pop(
                random.randint(0, len(self.number_list)-1))
        else:
            return None

    def is_win(self, num):
        """Проверка условия победы"""
        print(f'Вы загодали {num}?')
        answer = (input('Введите "y" если да, либо любой символ: '))
        if answer.lower() == 'y':
            return True

        return False

    def end_game(self, num):
        """Это конец игры"""
        print('----------------------------------------------')
        print((f'Ура! ПК угадал число {num}'
               f' за {self.try_count} попыток!'))
        print('----------------------------------------------')

    def cheat(self):
        print('Обманывать ПК не хорошо!')
        print('Запускаю команду format C:/')
        time.sleep(1)
        print('.')
        time.sleep(2)
        print('...')
        time.sleep(1)
        print('.....')
        time.sleep(2)
        print('..........')
        time.sleep(1)
        print('.................')
        time.sleep(3)
        print('Шутка! Му-ха-ха!')


if __name__ == '__main__':
    game = Game()
    game.start()
