"""Функция random_numbers()
Реализуйте функцию random_numbers(), которая принимает два аргумента:
left — целое число
right — целое число
Функция должна возвращать итератор, генерирующий бесконечную последовательность случайных целых чисел
в диапазоне от left до right включительно.
Примечание 1. Гарантируется, что left <= right.
"""
from random import randint


def random_numbers(left, right):
    def callable_func():
        return randint(left, right)

    return iter(callable_func, '')


for i in range(100):
    print(next(random_numbers(0, 100)))
