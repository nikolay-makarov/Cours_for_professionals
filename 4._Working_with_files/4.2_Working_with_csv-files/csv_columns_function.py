"""
Функция csv_columns()
Реализуйте функцию csv_columns(), которая принимает один аргумент:
filename — название csv файла, например, data.csv
Функция должна возвращать словарь, в котором ключом является название столбца файла filename,
а значением — список элементов этого столбца.
Примечание 1. Гарантируется, что в передаваемом в функцию файле разделителем является запятая,
при этом кавычки не используются.
Примечание 2. Гарантируется, что у передаваемого в функцию файла первая строка содержит названия столбцов.
Примечание 3. Например, если бы файл exam.csv имел вид:
name,grade
Timur,5
Arthur,4
Anri,5
то следующий вызов функции csv_columns():
csv_columns('exam.csv')
должен был бы вернуть:
{'name': ['Timur', 'Arthur', 'Anri'], 'grade': ['5', '4', '5']}
Примечание 4. Ключи в словаре, а также элементы в списках должны располагаться в своем исходном порядке.
"""
import csv


def csv_columns(filename):
    result = {}
    with open(filename, 'r', encoding='utf-8-sig', newline='') as file:
        data = csv.DictReader(file)
        for dict_ in data:
            for key, value in dict_.items():
                result.setdefault(key, []).append(value)
    return result


def csv_columns2(filename):
    with open(filename, encoding="utf-8") as file:
        rows = list(csv.reader(file))
        return {key: value for key, *value in zip(*rows)}


print(csv_columns('file.txt'))
