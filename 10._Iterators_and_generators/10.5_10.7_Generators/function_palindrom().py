"""Функция palindromes()
Реализуйте генераторную функцию palindromes(), которая не принимает никаких аргументов.
Функция должна возвращать генератор, порождающий бесконечную последовательность натуральных чисел-палиндромов.
Примечание 1. Число-палиндром — число, которое читается одинаково как справа налево, так и слева направо.
"""


def palindromes():
    number = 1
    while True:
        if str(number) == str(number)[::-1]:
            yield number
        number += 1


generator = palindromes()
numbers = [next(generator) for _ in range(30)]

print(*numbers)