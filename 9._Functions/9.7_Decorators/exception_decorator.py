"""Декоратор exception_decorator
Реализуйте декоратор exception_decorator, который возвращает
- кортеж (value, 'Функция выполнилась без ошибок'), если декорируемая функция завершила свою работу без ошибок,
где value — возвращаемое значение декорируемой функции
- кортеж (None, 'При вызове функции произошла ошибка'), если при выполнении декорируемой функции возникла ошибка
"""


def exception_decorator(func: any):
    def wrapper(*args: any, **kwargs: any):
        try:
            value = func(*args, **kwargs)
        except Exception:
            return None, 'При вызове функции произошла ошибка'
        return value, 'Функция выполнилась без ошибок'

    return wrapper


@exception_decorator
def f(x):
    return x ** 2 + 2 * x + 1


print(f(7))  # (64, 'Функция выполнилась без ошибок')


sum = exception_decorator(sum)
print(sum(['199', '1', 187]))  # (None, 'При вызове функции произошла ошибка')
