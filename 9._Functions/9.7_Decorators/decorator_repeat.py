"""Декоратор repeat
Реализуйте декоратор repeat, который принимает один аргумент:

- times — натуральное число
Декоратор должен вызывать декорируемую функцию times раз.
Также декоратор должен сохранять имя и строку документации декорируемой функции.
"""
import functools


def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times - 1):
                func(*args, **kwargs)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def say_beegeek():
    """documentation."""
    print('beegeek')


say_beegeek()


@repeat(4)
def say_beegeek():
    """"documentation"""
    print('beegeek')


print(say_beegeek.__name__)
print(say_beegeek.__doc__)