"""Функция is_good_password() 👀
Назовем пароль хорошим, если
    его длина равна 9 или более символам,
    в нем присутствуют большие и маленькие буквы любого алфавита,
    в нем имеется хотя бы одна цифра.
Реализуйте функцию is_good_password() в стиле LBYL, которая принимает один аргумент:
    string — произвольная строка
Функция должна возвращать True, если строка string представляет собой хороший пароль, или False в противном случае.
"""


def is_good_password(string: str) -> bool:
    if isinstance(string, str):
        is_lower = False
        is_upper = False
        is_digit = False
        is_long = len(string) >= 9
        for symbol in string:
            if symbol.isdigit():
                is_digit = True
            elif symbol.islower():
                is_lower = True
            elif symbol.isupper():
                is_upper = True
        return is_long and is_upper and is_lower and is_digit
    else:
        return False


print(is_good_password('41157082'))
print(is_good_password('мойпарольсамыйлучший'))
print(is_good_password('МойПарольСамыйЛучший111'))
