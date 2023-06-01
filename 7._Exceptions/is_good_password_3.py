"""Уж лучше матрицы 😐
Назовем пароль хорошим, если
    его длина равна 9 или более символам,
    в нем присутствуют большие и маленькие буквы любого алфавита,
    в нем имеется хотя бы одна цифра.
Напишите программу, которая требует ввода нового пароля до тех пор, пока не будет введен хороший.
Формат входных данных
На вход программе подается произвольное количество паролей, каждый на отдельной строке.
Гарантируется, что среди них присутствует хороший.
Формат выходных данных
Для каждого введенного пароля программа должна вывести текст:
    LengthError, если длина введенного пароля меньше 99 символов
    LetterError, если в нем все буквы имеют одинаковый регистр либо отсутствуют
    DigitError, если в нем нет ни одной цифры
    Success!, если введенный пароль хороший
После ввода хорошего пароля все последующие пароли должны игнорироваться.
Примечание 1. Приоритет вывода сообщений об ошибке в случае невыполнения нескольких условий:
LengthError, затем LetterError, а уже после DigitError.
Примечание 2. Воспользуйтесь функцией is_good_password() из предыдущей задачи.
"""
import sys


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


def is_good_password(string: str) -> bool:
    if len(string) < 9:
        raise LengthError('LengthError')
    if not (any(char.isupper() for char in string) and any(char.islower() for char in string)):
        raise LetterError('LetterError')
    if not any(char.isdigit() for char in string):
        raise DigitError('DigitError')
    return True


passwords = sys.stdin.read().splitlines()
for password in passwords:
    try:
        if is_good_password(password):
            print('Success!')
            break
    except Exception as e:
        print(e)
