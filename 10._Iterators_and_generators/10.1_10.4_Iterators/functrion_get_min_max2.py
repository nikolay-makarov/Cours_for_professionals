"""Функция get_min_max() 😳
Реализуйте функцию get_min_max(), которая принимает один аргумент:
iterable — итерируемый объект, элементы которого сравнимы между собой
Функция должна возвращать кортеж, в котором первым элементом является минимальный элемент итерируемого объекта iterable,
вторым — максимальный элемент итерируемого объекта iterable.
Если итерируемый объект iterable пуст, функция должна вернуть значение None.
"""


def get_min_max(iterable):
    try:
        new_iter = iter(iterable)
        min_obj = next(new_iter)
        max_obj = min_obj
        for elem in new_iter:
            if elem < min_obj:
                min_obj = elem
            if elem > max_obj:
                max_obj = elem
        return min_obj, max_obj
    except Exception:
        return None


iterable = iter(range(10))
print(get_min_max(iterable))  # (0, 9)

iterable = [6, 4, 2, 33, 19, 1]
print(get_min_max(iterable))  # (1, 33)

iterable = iter([])
print(get_min_max(iterable))  # None
