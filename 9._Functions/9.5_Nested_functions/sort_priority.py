"""Функция sort_priority() 🌶️
Реализуйте функцию sort_priority(), которая принимает два аргумента в следующем порядке:
    values — список чисел
    group — список, кортеж или множество чисел
Функция должна сортировать по неубыванию список чисел values,
делая при этом приоритетной группу чисел из group, которая должна следовать первой.
"""


def sort_priority(values, group):
    def comparator(elem):
        if elem in group:
            return 0, elem
        return 1, elem
    values.sort(key=comparator)


numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
sort_priority(numbers, (300, 100, 200))
assert numbers == [1, 2, 3, 4, 5, 6, 7, 8, 9], 'Решение с ошибкой!'
print(numbers)


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {5, 7, 2, 3}
sort_priority(numbers, group)
assert numbers == [2, 3, 5, 7, 1, 4, 6, 8], 'Решение с ошибкой!'
print(numbers)
