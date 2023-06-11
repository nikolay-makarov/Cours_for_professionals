"""Функция get_all_values() 🌶️
Реализуйте функцию get_all_values(), которая принимает два аргумента в следующем порядке:
- nested_dicts — словарь, содержащий в качестве значений произвольные объекты или словари, которые, в свою очередь,
так же содержат в качестве значений произвольные объекты или словари; вложенность может быть произвольной.
- key — хешируемый объект
Функция должна определять все значения, которые соответствуют ключу key в словаре nested_dicts
и всех его вложенных словарях, и возвращать их в виде множества.
Если ключа key нет ни в одном словаре, функция должна вернуть пустое множество.
"""


def get_all_values(nested_dicts, key):
    pass


my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
result = get_all_values(my_dict, 'top_grade')

print(*sorted(result))
