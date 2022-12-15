"""Функция get_all_mondays()
Реализуйте функцию get_all_mondays(), которая принимает один аргумент:
year — натуральное число
Функция должна возвращать отсортированный по возрастанию список всех дат (тип date) года year, выпадающих на понедельник.
Примечание 1. Например, вызов:
get_all_mondays(2021)
должен вернуть список:
[datetime.date(2021, 1, 4), datetime.date(2021, 1, 11), ...,
datetime.date(2021, 12, 20), datetime.date(2021, 12, 27)]"""
import calendar
from datetime import timedelta, date


def get_all_mondays(year: int) -> list[date]:
    first_day = calendar.weekday(year, 1, 1)
    if first_day != 0:
        first_monday = 8 - first_day
    else:
        first_monday = 1
    date_ = date(year, 1, first_monday)
    result = []
    while date_.year == year:
        result.append(date_)
        date_ += timedelta(days=7)
    return result


# print(get_all_mondays(2021))
