"""Функция hash_as_key()
Реализуйте функцию hash_as_key(), которая принимает один аргумент:
objects — список хешируемых объектов.
Функция должна возвращать словарь, ключом в котором является хеш-значение объекта из списка objects,
а значением — сам объект. Если хеш-значения некоторых объектов совпадают, их следует объединить в список.
Примечание 1. Элементы в возвращаемом функцией словаре, а также объекты в списке, имеющие равные хеш-значения,
должны располагаться в своем исходном порядке.
"""
from collections import defaultdict


def hash_as_key(objects: list[any]) -> dict:
    result = defaultdict(list)
    for obj in objects:
        result[hash(obj)].append(obj)
    return {k: v[0] if len(v) == 1 else v for k, v in result.items()}


data = [5, 5, 3, 1, 8, -1, -2, 5]
print(hash_as_key(data))
