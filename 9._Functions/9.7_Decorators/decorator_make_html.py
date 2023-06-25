"""Декоратор make_html
Тег — элемент языка разметки, используемый для форматирования текста.
Например, текст, заключённый между начальным тегом <small> и конечным тегом </small>, отображается с меньшим размером,
чем основной текст, а текст между тегами <big> и </big> отображается с большим размером.
Реализуйте декоратор make_html(), который принимает один аргумент:
tag — HTML-тег, например, del
Декоратор должен обрамлять возвращаемое значение декорируемой функции в HTML-тег tag.
Также декоратор должен сохранять имя и строку документации декорируемой функции.
Примечание 1. Гарантируется, что возвращаемым значением декорируемой функции является объект типа str.
"""
import functools


def make_html(tag):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            return f'<{tag}>{value}</{tag}>'

        return wrapper

    return decorator


@make_html('del')
def get_text(text):
    return text


print(get_text('Python'))


@make_html('i')
@make_html('del')
def get_text(text):
    return text


print(get_text(text='decorators are so cool!'))
