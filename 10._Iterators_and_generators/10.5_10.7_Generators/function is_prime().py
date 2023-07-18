"""Функция is_prime()
Реализуйте функцию is_prime() с использованием генераторных выражений, которая принимает один аргумент:
number — натуральное число
Функция должна возвращать True, если число number является простым, или False в противном случае.
"""


def is_prime(number):
    if number == 1:
        return False
    return all(bool(number % div) for div in range(2, round(number ** 0.5) + 1))


print(is_prime(7))
print(is_prime(8))
