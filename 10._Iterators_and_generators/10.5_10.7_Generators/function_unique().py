"""Функция unique()
Реализуйте генераторную функцию, которая принимает один аргумент:
iterable — итерируемый объект
Функция должна возвращать генератор, порождающий последовательность элементов
итерируемого объекта iterable без дубликатов.
Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе
должны располагаться в своем исходном порядке.
"""


def unique(iterable):
    yield from {elem: None for elem in iterable}


numbers = [1, 2, 2, 3, 4, 5, 5, 5]
print(*unique(numbers))

iterator = iter('111222333')
uniques = unique(iterator)

print(next(uniques))
print(next(uniques))
print(next(uniques))
