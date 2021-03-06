"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать где какая сложность.

Примечание:
Построить список можно через списковое включение.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""
from random import randint


def list_min_number(my_list):
    for i in my_list:
        is_min = True
        for j in my_list:
            if i > j:
                is_min = False
        if is_min:
            return i


def list_min_num(my_list):
    min_num = my_list[0]
    for i in my_list:
        if i < min_num:
            min_num = i
    return min_num


my_list = [randint(0, 50) for i in range(15)]
print(my_list)
print(list_min_number(my_list))
print(list_min_num(my_list))
