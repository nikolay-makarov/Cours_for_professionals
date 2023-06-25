"""Декоратор takes_positive
Реализуйте декоратор takes_positive, который проверяет, что все аргументы, передаваемые в декорируемую функцию,
являются положительными целыми числами.
Если хотя бы один аргумент не удовлетворяет данному условию, декоратор должен возбуждать исключение:
TypeError, если аргумент не является целым числом
ValueError, если аргумент является целым числом, но отрицательным или равным нулю
Примечание 1. Приоритет возбуждения исключений при несоответствии аргумента обоим условиям
или при наличии разных аргументов, несоответствующих разным условиям: TypeError, затем ValueError.
"""


def takes_positive(func):
    def wrapper(*args, **kwargs):
        is_integer = all([isinstance(elem, int) for elem in list(args) + list(kwargs.values())])
        is_positive = all(elem > 0 for elem in list(args) + list(kwargs.values()))
        if not is_integer:
            raise TypeError
        if not is_positive:
            raise ValueError
        return func(*args, **kwargs)

    return wrapper


@takes_positive
def positive_sum(*args):
    return sum(args)


assert positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) == 55
print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum(-3, -2, -1, 0, 1, 2, 3))
except Exception as err:
    assert type(err).__name__ == 'ValueError'
    print(type(err))


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum('10', 20, 10))
except Exception as err:
    assert type(err).__name__ == 'TypeError'
    print(type(err))
