"""Функция filter_names()
Реализуйте генераторную функцию filter_names(), которая принимает три аргумента в следующем порядке:
names — список имен
ignore_char — одиночный символ
max_names — натуральное число
Функция должна возвращать генератор, порождающий max_names имён из списка names, игнорируя имена, которые
начинаются на ignore_char (в любом регистре)
содержат хотя бы одну цифру
Если max_names больше количества имен в списке names,
то генератор должен породить все возможные имена из данного списка.
Примечание 1. Имена в возвращаемом функцией генераторе должны располагаться в своем исходном порядке.
"""


def filter_names(names: list[str], ignore_char: str, max_names: int):
    result = (name for name in names if not name.lower().startswith(ignore_char.lower()) and name.isalpha())
    for number, name in enumerate(result, 1):
        if number <= max_names:
            yield name


data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']
print(*filter_names(data, 'D', 3))  # Timur Arthur Arina

data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']
print(*filter_names(data, 't', 20))  # Dima Arthur Arina German Ruslan
