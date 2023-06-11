"""Необычная сортировка 🌶️
Дана строка, содержащая латинские буквы и цифры.
Напишите программу, которая сортирует символы в строке согласно следующим правилам:
все отсортированные строчные буквы стоят перед заглавными буквами
все отсортированные заглавные буквы стоят перед цифрами
все отсортированные нечетные цифры стоят перед отсортированными четными
Формат входных данных
На вход программе подается строка, содержащая латинские буквы и цифры.
Формат выходных данных
Программа должна расположить символы в строке в соответствии с условием задачи и вывести полученный результат.
"""
string = input()
lowercase, capital, even, odd = [], [], [], []
for symbol in string:
    if symbol.islower():
        lowercase.append(symbol)
    elif symbol.isupper():
        capital.append(symbol)
    elif symbol.isdigit():
        if not int(symbol) % 2:
            even.append(symbol)
        else:
            odd.append(symbol)
print(''.join(
    sorted(lowercase) + sorted(capital) + sorted(odd, key=lambda x: int(x)) + sorted(even, key=lambda x: int(x))))
