"""Функция dates()
Реализуйте генераторную функцию dates(), которая принимает два аргумента в следующем порядке:
start — дата, тип date;
count — натуральное число, по умолчанию имеет значение None.
Если count имеет значение None, функция должна возвращать генератор,
порождающий последовательность из максимально допустимого количества дат (тип date), начиная с даты start.
Если count имеет в качестве значения натуральное число,
функция должна возвращать генератор, порождающий последовательность из count дат (тип date),
начиная с даты start, а затем возбуждающий исключение StopIteration.
"""
from datetime import date


def dates(start: date, count: int | None = None):
    try:
        start_number = start.toordinal()
        while count != 0:
            if (gen_date := date.fromordinal(start_number)) <= date.max:
                yield gen_date
                start_number += 1
                if count is not None:
                    count -= 1
            else:
                break
    except ValueError:
        pass


print(date.max)
generator = dates(date(9999, 1, 7), 500)

for _ in range(348):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

try:
    print(next(generator))
except StopIteration:
    print('Error')
