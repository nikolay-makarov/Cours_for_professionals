"""Функция get_the_fastest_func()
Реализуйте функцию get_the_fastest_func(), которая принимает два аргумента в следующем порядке:
- funcs — список произвольных функций
- arg — произвольный объект
Функция get_the_fastest_func() должна возвращать функцию из списка funcs,
которая затратила на вычисление значения при вызове с аргументом arg наименьшее количество времени.
"""
import time


def get_the_fastest_func(funcs: list, arg: any):
    performance_dict: dict = {}
    for func in funcs:
        start = time.perf_counter()
        func(arg)
        stop = time.perf_counter()
        performance_dict[stop - start] = func
    return performance_dict[min(performance_dict)]
