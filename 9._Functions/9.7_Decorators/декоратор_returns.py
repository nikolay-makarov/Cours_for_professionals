"""Декоратор returns
Реализуйте декоратор returns, который принимает один аргумент:
datatype — тип данных
Декоратор должен проверять, что возвращаемое значение декорируемой функции принадлежит типу datatype.
Если возвращаемое значение принадлежит какому-либо другому типу, декоратор должен возбуждать исключение TypeError.
Также декоратор должен сохранять имя и строку документации декорируемой функции.
"""
import functools


def returns(datatype):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not isinstance(result, datatype):
                raise TypeError
            return result

        return wrapper

    return decorator


@returns(int)
def add(a, b):
    return a + b


print(add(10, 5))


@returns(int)
def add(a, b):
    return a + b


try:
    print(add('199', '1'))
except TypeError as e:
    print(type(e))


@returns(list)
def beegeek():
    """beegeek docs"""
    return 'beegeek'


print(beegeek.__name__)
print(beegeek.__doc__)

try:
    print(beegeek())
except TypeError as e:
    print(type(e))


@returns(list)
def append_this(li, elem):
    """append_this docs"""
    return li + [elem]


print(append_this.__name__)
print(append_this.__doc__)
print(append_this([1, 2, 3], elem=4))
