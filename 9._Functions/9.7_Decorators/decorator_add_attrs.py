"""Декоратор add_attrs
Реализуйте декоратор add_attrs, который принимает произвольное количество именованных аргументов
и устанавливает их в качестве атрибутов декорируемой функции.
Названием атрибута должно являться имя аргумента, значением атрибута — значение аргумента.
Также декоратор должен сохранять имя и строку документации декорируемой функции.
Примечание 1. Вспомните про атрибут функции __dict__.
"""
import functools


def add_attrs(**kwargs_):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        for key, value in kwargs_.items():
            wrapper.__dict__[key] = value
        return wrapper

    return decorator


@add_attrs(attr2='geek')
@add_attrs(attr1='bee')
def beegeek():
    return 'beegeek'


print(beegeek.attr1)
print(beegeek.attr2)
print(beegeek.__name__)
