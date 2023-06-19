"""Функция cyclic_shift()
Реализуйте функцию cyclic_shift() с использованием аннотаций типов, которая принимает два аргумента в следующем порядке:
numbers — список целых или вещественных чисел
step — целое число
Функция должна изменять переданный список, циклически сдвигая элементы списка на step шагов,
и возвращать значение None.
Если step является положительным числом, сдвиг происходит вправо, если отрицательным — влево.
"""


def cyclic_shift(numbers: list[int | float], step: int) -> None:
    if step > 0:
        for _ in range(step):
            numbers.insert(0, numbers.pop())
    else:
        for _ in range(abs(step)):
            numbers.append(numbers.pop(0))


numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, 1)
print(numbers)  # [5, 1, 2, 3, 4]

numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, -2)
print(numbers)  # [3, 4, 5, 1, 2]
