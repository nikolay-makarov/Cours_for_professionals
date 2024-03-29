"""Структура архива 🌶️🌶️
Вам доступен архив desktop.zip, содержащий различные папки и файлы.
Напишите программу, которая выводит его файловую структуру и объем каждого файла.
Формат входных данных
На вход программе ничего не подается.
Формат выходных данных
Программа должна вывести файловую структуру архива desktop.zip и объем каждого файла в несжатом виде.
Так как архив имеет собственную иерархию папок, каждый уровень вложенности должен быть выделен двумя пробелами.
Примечание 1. Вывод на примере архива test.zip из конспекта:
test
  Картинки
    1.jpg 88 KB
    avatar.png 19 KB
    certificate.png 43 KB
    py.png 33 KB
    World_Time_Zones_Map.png 2 MB
    Снимок экрана.png 11 KB
  Неравенства.djvu 5 MB
  Программы
    image_util.py 5 KB
    sort.py 61 B
  Разные файлы
    astros.json 505 B
Примечание 2. Объем файла записывается в самых крупных единицах измерения с округлением до целых.
Примечание 3. Значения единиц измерения такие же, какие приняты в информатике:
    1 KB = 1024 B
    1 MB = 1024 KB
    1 GB = 1024 MB
"""
from zipfile import ZipFile


def get_filesize(size: int) -> str:
    if 0 < size < 1024:
        return f'{size} B'
    elif 1024 <= size < 1024 ** 2:
        return f'{round(size / 1024)} KB'
    elif 1024 ** 2 <= size < 1024 ** 3:
        return f'{round(size / 1024 ** 2)} MB'


with ZipFile('files/desktop.zip') as zip_file:
    names_list = zip_file.namelist()
    for name_list in names_list:
        path_list = name_list.rstrip('/').split('/')
        if zip_file.getinfo(name_list).is_dir():
            print(f"{'  ' * (len(path_list) - 1)}{path_list[-1]}")
        else:
            print(f"{'  ' * (len(path_list) - 1)}{path_list[-1]} "
                  f"{get_filesize(zip_file.getinfo(name_list).file_size)}")
