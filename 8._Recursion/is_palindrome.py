"""Функция is_palindrome()
Реализуйте функцию is_palindrome() с использованием рекурсии, которая принимает один аргумент:
- string — произвольная строка
Функция должна возвращать значение True, если переданная строка является палиндромом, или False в противном случае.
Примечание 1. Палиндром — текст, одинаково читающийся в обоих направлениях.
Примечание 2. Пустая строка является палиндромом, как и строка, состоящая из одного символа.
"""


def is_palindrome(string: str) -> bool:
    if not string or len(string) == 1:
        return True
    elif string[0] != string[-1]:
        return False
    else:
        return is_palindrome(string[1:-1])


print(is_palindrome('stepik'))
print(is_palindrome('level'))
print(is_palindrome('122333221'))
