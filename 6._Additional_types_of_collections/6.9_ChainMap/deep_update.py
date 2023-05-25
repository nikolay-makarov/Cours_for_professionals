"""Функция deep_update()
Реализуйте функцию deep_update(), которая принимает три аргумента в следующем порядке:
    chainmap — объект типа ChainMap, элементами которого являются словари
    key — хэшируемый объект
    value — произвольный объект
Функция должна изменять все значения по ключу key во всех словарях в chainmap на value.
Если ключ key отсутствует в chainmap, функция должна добавить пару key: value в первый словарь.
Примечание 1. Функция должна изменять передаваемый объект типа ChainMap и возвращать значение None.
Примечание 2. Гарантируется, что передаваемый в функцию объект типа ChainMap содержит хотя бы один словарь.
"""
from collections import ChainMap


def deep_update(chainmap: ChainMap, key, value) -> None:
    if key not in chainmap:
        chainmap[key] = value
    else:
        for dict_ in chainmap.maps:
            if key in dict_:
                dict_[key] = value


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
deep_update(chainmap, 'age', 20)

print(chainmap)
