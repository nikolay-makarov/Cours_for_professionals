"""Функция recursive_sum()
Реализуйте recursive_sum() с использованием рекурсии, которая принимает один аргумент:
nested_lists — список, элементами которого являются целые числа или списки, элементами которых, в свою очередь,
также являются либо целые числа, либо списки; вложенность может быть произвольной
Функция должна вычислять сумму всех чисел во всех списках и возвращать полученный результат.
Если список nested_lists пуст, функция должна вернуть число 0.
"""


def recursive_sum(nested_lists: list[int, list]) -> int:
    result = 0
    for elem in nested_lists:
        if isinstance(elem, list):
            elem = recursive_sum(elem)
        result += elem
    return result


my_list = [1, [4, 4], 2, [1, [2, 10]]]
print(recursive_sum(my_list))

my_list = []
print(recursive_sum(my_list))
