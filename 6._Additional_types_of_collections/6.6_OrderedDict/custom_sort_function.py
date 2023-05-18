"""Функция custom_sort() 🌶️
Реализуйте функцию custom_sort(), которая принимает два аргумента в следующем порядке:
    ordered_dict — словарь OrderedDict
    by_values — булево значение, по умолчанию имеет значение False
Функция должна сортировать словарь ordered_dict:
    по ключам, если by_values имеет значение False
    по значениям, если by_values имеет значение True
Примечание 1. Функция должна изменять переданный словарь, а не возвращать новый.
Возвращаемым значением функции должно быть None.
Примечание 2. Гарантируется, что переданный в функцию словарь можно отсортировать, то есть он не содержит ключи,
имеющие разные типы, а также значения, имеющие разные типы.
Примечание 3. Если два элемента имеют равные значения, то следует сохранить их исходный порядок следования.
"""
from collections import OrderedDict


def custom_sort(ordered_dict: OrderedDict, by_values: bool = False) -> None:
    for key, _ in sorted(ordered_dict.items(), key=lambda x: x[by_values]):
        ordered_dict.move_to_end(key)

    # if by_values:
    #     for key, _ in sorted(ordered_dict.items(), key=lambda x: x[1]):
    #         ordered_dict.move_to_end(key)
    # else:
    #     for key in sorted(ordered_dict):
    #         ordered_dict.move_to_end(key)


data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
custom_sort(data)
print(data)

data = OrderedDict(Earth=3, Mercury=1, Mars=4, Venus=2)
custom_sort(data, by_values=True)
print(*data.items())
