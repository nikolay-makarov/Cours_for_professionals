"""Форматированный вывод
Вам доступен архив workbook.zip, содержащий различные папки и файлы.
Напишите программу, которая выводит названия всех файлов из этого архива в лексикографическом порядке,
указывая для каждого его дату изменения, а также объем до и после сжатия, в следующем формате:
<название файла>
  Дата модификации файла: <дата изменения>
  Объем исходного файла: <объем до сжатия> байт(а)
  Объем сжатого файла: <объем после сжатия> байт(а)
Между данными о двух файлах должна располагаться пустая строка.
Примечание 1. Если файл находится в папке, вывести следует только название без пути.
"""
from datetime import datetime
from pathlib import Path
from zipfile import ZipFile

with ZipFile('files/workbook.zip', mode='r') as zip_file:
    info_list = zip_file.infolist()

for info in sorted(info_list, key=lambda x: Path(x.filename).name):
    if not info.is_dir():
        print(Path(info.filename).name)
        print(f'  Дата модификации файла: {datetime(*info.date_time)}')
        print(f'  Объем исходного файла: {info.file_size} байт(а)')
        print(f'  Объем сжатого файла: {info.compress_size} байт(а)\n')
