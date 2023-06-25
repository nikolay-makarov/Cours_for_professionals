"""Декоратор prefix
Реализуйте декоратор prefix, который принимает два аргумента в следующем порядке:
    string — произвольная строка
    to_the_end — булево значение, по умолчанию равное False
Декоратор должен добавлять строку string к возвращаемому значению декорируемой функции.
Если to_the_end имеет значение True, строка string добавляется в конец, если False — в начало.
Также декоратор должен сохранять имя и строку документации декорируемой функции.
Примечание 1. Гарантируется, что возвращаемым значением декорируемой функции является объект типа str.
"""
import functools


def prefix(string: str, to_the_end: bool = False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if to_the_end:
                return func(*args, **kwargs) + string
            return string + func(*args, **kwargs)

        return wrapper

    return decorator


@prefix('€')
def get_bonus():
    return '2000'


print(get_bonus())


@prefix('$$$', to_the_end=True)
def get_bonus():
    return '2000'


print(get_bonus())
