"""Функция get_value()
Реализуйте функцию get_value(), которая принимает три аргумента в следующем порядке:
    chainmap — объект типа ChainMap, элементами которого являются словари
    key — произвольный объект
    from_left — булево значение, по умолчанию равное True
Функция должна возвращать значение по ключу key из chainmap, причем:
    если from_left имеет значение True, поиск ключа в chainmap должен происходить от первого словаря к последнему
    если from_left имеет значение False, поиск ключа в chainmap должен происходить от последнего словаря к первому
Если ключ key отсутствует в chainmap, функция должна вернуть значение None.
"""
from collections import ChainMap


def get_value(chainmap: ChainMap, key, from_left: bool = True):
    if from_left:
        return chainmap.get(key)
    else:
        return ChainMap(*chainmap.maps[::-1]).get(key)


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'age'))
