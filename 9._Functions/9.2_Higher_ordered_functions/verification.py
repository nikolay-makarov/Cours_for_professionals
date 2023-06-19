"""Функция verification()
Реализуйте функцию verification(), которая проверяет правильность введенного пароля.
Она должна принимать четыре аргумента в следующем порядке:
    login — логин пользователя
    password — пароль пользователя
    success — некоторая функция
    failure — некоторая функция
Пароль считается правильным, если в нем присутствует, хотя бы одна заглавная латинская буква,
хотя бы одна строчная латинская буква и хотя бы одна цифра.
Функция verification() должна вызывать функцию success() с аргументом login,
если переданный пароль является правильным, иначе — функцию failure() с аргументами login
и строкой-сообщением об ошибке:
    в пароле нет ни одной буквы, если в пароле отсутствуют латинские буквы
    в пароле нет ни одной заглавной буквы, если в пароле отсутствуют заглавные латинские буквы
    в пароле нет ни одной строчной буквы, если в пароле отсутствуют строчные латинские буквы
    в пароле нет ни одной цифры, если в пароле отсутствуют цифры
Примечание 1. Если пароль не удовлетворяет нескольким условиям,
то приоритеты выбора строки-сообщения об ошибке являются следующими:
    в пароле нет ни одной буквы
    в пароле нет ни одной заглавной буквы
    в пароле нет ни одной строчной буквы
    в пароле нет ни одной цифры
"""
from string import ascii_letters


def verification(login: str, password: str, success, failure):
    has_letters, has_upper, has_lower, has_digit = False, False, False, False
    for symbol in password:
        if symbol in ascii_letters:
            has_letters = True
        if has_letters and symbol.islower():
            has_lower = True
        elif has_letters and symbol.isupper():
            has_upper = True
        elif symbol.isdigit():
            has_digit = True
    if all((has_letters, has_upper, has_lower, has_digit)):
        success(login)
    if not has_letters:
        failure(login, 'в пароле нет ни одной буквы')
    elif not has_upper:
        failure(login, 'в пароле нет ни одной заглавной буквы')
    elif not has_lower:
        failure(login, 'в пароле нет ни одной строчной буквы')
    elif not has_digit:
        failure(login, 'в пароле нет ни одной цифры')


def success(login):
    print(f'Здравствуйте, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Arthur_Davletov', 'мойпарольBEE123', success, failure)
