"""Итератор RandomNumbers
Реализуйте класс RandomNumbers, порождающий итераторы, конструктор которого принимает три аргумента в следующем порядке:
left — целое число
right — целое число
n — натуральное число
Итератор класса RandomNumbers должен генерировать последовательность из n случайных чисел
от left до right включительно, а затем возбуждать исключение StopIteration.
Примечание 1. Гарантируется, что left <= right.
"""
from random import randint


class RandomNumbers:
    def __init__(self, left: int, right: int, n: int) -> None:
        self.left: int = left
        self.right: int = right
        self.n: int = n

    def __iter__(self) -> 'RandomNumbers':
        return self

    def __next__(self) -> int:
        if self.n <= 0:
            raise StopIteration
        self.n -= 1
        return randint(self.left, self.right)


iterator = RandomNumbers(-1000, -900, 1)

print(next(iterator) in range(-1000, -899))
try:
    next(iterator)
except StopIteration:
    print('Error')
