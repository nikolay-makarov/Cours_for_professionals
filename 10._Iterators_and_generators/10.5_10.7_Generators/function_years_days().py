"""Функция years_days()
Реализуйте генераторную функцию years_days(), которая принимает один аргумент:
year — натуральное число
Функция должна возвращать генератор, порождающий последовательность всех дат (тип date) в году year.
Примечание 1. Возьмем в качестве примера 20222022 год. В январе этого года 3131 день, в феврале — 2828,
в марте — 3131, и так далее. Тогда генератор, полученный при вызове years_days(2022),
должен порождать сначала все даты с 1 по 31 января, затем с 1 по 28 февраля, и так далее до 31 декабря.
"""
from datetime import date, timedelta


def years_days(year: int):
    day = date(year, 1, 1)
    while day.year == year:
        yield day
        day += timedelta(days=1)


dates = years_days(2022)

print(next(dates))
print(next(dates))
print(next(dates))
print(next(dates))
