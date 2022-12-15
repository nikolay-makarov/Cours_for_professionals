"""Функция get_days_in_month()
Реализуйте функцию get_days_in_month(), которая принимает два аргумента в следующем порядке:
year — натуральное число
month — полное название месяца на английском
Функция должна возвращать отсортированный по возрастанию список всех дат (тип date) месяца month и года year.
Примечание 1. Например, вызов:
get_days_in_month(2021, 'December')
должен вернуть список:
[datetime.date(2021, 12, 1), datetime.date(2021, 12, 2), ...,
datetime.date(2021, 12, 30), datetime.date(2021, 12, 31)]"""
import calendar
import datetime


def get_days_in_month(year: int, month_name: str) -> list[datetime.date]:
    month_number: int = list(calendar.month_name).index(month_name)
    number_of_days: int = calendar.monthrange(year, month_number)[1]
    return [datetime.date(year, month_number, day)
            for day
            in range(1, number_of_days + 1)]

# print(get_days_in_month(2021, 'December'))
