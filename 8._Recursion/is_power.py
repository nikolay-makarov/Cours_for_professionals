"""Функция is_power()
Реализуйте функцию is_power() с использованием рекурсии, которая принимает один аргумент:
    number — натуральное число
Функция должна возвращать значение True, если number является степенью числа 2, или False в противном случае.
"""


def is_power(number: int) -> bool:
    if number == 1:
        return True
    elif not number % 2:
        return is_power(number // 2)
    return False


print(is_power(512))
print(is_power(15))
print(is_power(1))
