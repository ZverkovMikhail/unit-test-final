"""entry point into the final work application"""
# Задание 1. Создайте программу на Python или Java, которая принимает два списка чисел и выполняет
# следующие действия:
#  Рассчитывает среднее значение каждого списка.
#  Сравнивает эти средние значения и выводит соответствующее сообщение:
# - ""Первый список имеет большее среднее значение"", если среднее значение первого списка больше.
# - ""Второй список имеет большее среднее значение"", если среднее значение второго списка больше.
# - ""Средние значения равны"", если средние значения списков равны.
from list_averager import ListAverager


def print_answer(first_list, second_list):
    """method print answer of comp_averages result"""
    averager = ListAverager()
    try:
        match averager.comp_averages(first_list, second_list):
            case 0:
                print('Средние значения равны')
            case -1:
                print('Второй список имеет большее среднее значение')
            case 1:
                print('Первый список имеет большее среднее значение')
    except TypeError:
        print('Один из аргументов не является списком чисел')


if __name__ == '__main__':
    print_answer([1, 2, 3, 4], [32, 5, 67, 8])
    print_answer([100, 200, 30, 40], [32, 5, 67, 8])
    print_answer([40, 7, 64, 1], [32, 5, 67, 8])
    print_answer([40, 7, 64, 1], [32, 5, '67', 8])
