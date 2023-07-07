"""Функция filterfalse()
Реализуйте функцию filterfalse() с использованием функции filter(), которая принимает два аргумента:
predicate — функция-предикат; если имеет значение None, то работает аналогично функции bool()
iterable — итерируемый объект
Функция должна работать противоположно функции filter(), то есть возвращать итератор,
элементами которого являются элементы итерируемого объекта iterable,
для которых функция predicate вернула значение False.
Примечание 1. Предикат — это функция, которая возвращает True или False в зависимости
от переданного в качестве аргумента значения.
Примечание 2. Элементы итерируемого объекта в возвращаемом функцией итераторе должны располагаться
в своем исходном порядке.
Примечание 3. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
"""


def filterfalse(predicate, iterable):
    filtered = list(filter(predicate, iterable))
    return iter(i for i in iterable if i not in filtered)


objects = [0, 1, True, False, 17, []]
print(*filterfalse(None, objects))  # 0 False []

numbers = (1, 2, 3, 4, 5)
print(*filterfalse(lambda x: x % 2 == 0, numbers))  # 1 3 5

numbers = [1, 2, 3, 4, 5]
print(*filterfalse(lambda x: x >= 3, numbers))  # 1 2
