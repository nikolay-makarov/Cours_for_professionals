"""Декоратор takes
Реализуйте декоратор takes, который принимает произвольное количество позиционных аргументов,
каждый из которых является типом данных.
Декоратор должен проверять, что аргументы, передаваемые в декорируемую функцию, принадлежат одному из этих типов.
Если хотя бы один аргумент не принадлежит одному из данных типов, декоратор должен возбуждать исключение TypeError.
Также декоратор должен сохранять имя и строку документации декорируемой функции.
"""
import functools


def takes(*datatypes):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for arg in tuple(args) + tuple(kwargs.values()):
                if not isinstance(arg, datatypes):
                    raise TypeError
            return func(*args, **kwargs)
        return wrapper
    return decorator


@takes(int, str)
def repeat_string(string, times):
    return string * times

print(repeat_string('bee', 3))


@takes(list, bool, float, int)
def repeat_string(string, times):
    return string * times

try:
    print(repeat_string('bee', 4))
except TypeError as e:
    print(type(e))
