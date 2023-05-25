"""Функция get_all_values()
Реализуйте функцию get_all_values(), которая принимает два аргумента в следующем порядке:
- chainmap — объект типа ChainMap, элементами которого являются словари
- key — произвольный объект
Функция должна возвращать множество, элементами которого являются все значения по ключу key из всех словарей в chainmap.
Если ключ key отсутствует в chainmap, функция должна вернуть пустое множество.
Примечание 1. Гарантируется, что передаваемый в функцию объект типа ChainMap содержит словари с хешируемыми значениями.
"""
from collections import ChainMap


def get_all_values(chainmap: ChainMap, key) -> set:
    result = set()
    for dict_ in chainmap.maps:
        if key in dict_:
            result.add(dict_[key])
    return result


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
result = get_all_values(chainmap, 'age')

print(result)
