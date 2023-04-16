"""Избранные
Вам доступен архив workbook.zip, содержащий различные папки и файлы.
Напишите программу, которая выводит названия файлов из этого архива,
которые были созданы или изменены позднее 2021-11-30 14:22:00.
Названия файлов должны быть расположены в лексикографическом порядке, каждое на отдельной строке.
Примечание 1. Если файл находится в папке, вывести следует только название без пути.
"""
import datetime
from pathlib import Path
from zipfile import ZipFile

result = []
selected_date = datetime.datetime(2021, 11, 30, 14, 22)

with ZipFile('files/workbook.zip') as zip_file:
    info_list = zip_file.infolist()
    for file in info_list:
        if datetime.datetime(*file.date_time) >= selected_date and not file.is_dir():
            result.append(Path(file.filename).name)

print(*sorted(result), sep='\n')
