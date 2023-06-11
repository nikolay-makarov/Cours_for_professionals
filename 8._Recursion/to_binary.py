"""Функция to_binary()
Реализуйте функцию to_binary() с использованием рекурсии, которая принимает один аргумент:
number — неотрицательное целое число
Функция должна возвращать строковое представление числа number в двоичной системе счисления.
"""


def to_binary(number: int) -> str:
    if number == 0:
        return '0'
    result = []

    def recursion(n=number):
        if n != 0:
            result.append(str(n % 2))
            recursion(n // 2)

    recursion()
    return ''.join(reversed(result))


# Вариант 2:
# def to_binary(number: int) -> str:
#     if number <= 1:
#         return str(number)
#
#     return to_binary(number // 2) + str(number % 2)


print(to_binary(123))
