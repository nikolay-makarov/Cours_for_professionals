"""Функция get_min_max() 😎
Реализуйте функцию get_min_max(), которая принимает один аргумент:
data — список произвольных объектов, сравнимых между собой
Функция должна возвращать кортеж, в котором первым элементом является индекс минимального элемента в списке data,
вторым — индекс максимального элемента в списке data. Если список data пуст, функция должна вернуть значение None.
Примечание 1. Если минимальных / максимальных элементов несколько, следует вернуть индексы первого по порядку элемента.
"""


def get_min_max(data: list) -> tuple[int, int] | None:
    if data:
        min_index = min(enumerate(data), key=lambda x: x[1])[0]
        max_index = max(enumerate(data), key=lambda x: x[1])[0]
        return min_index, max_index


data = [2, 3, 8, 1, 7]
print(get_min_max(data))

data = [1, 1, 2, 3, 8, 8]
print(get_min_max(data))

data = []
print(get_min_max(data))
