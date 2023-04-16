"""Объем файлов
Вам доступен архив workbook.zip, содержащий различные папки и файлы.
Напишите программу, которая выводит суммарный объем файлов этого архива в сжатом и не сжатом видах в байтах,
в следующем формате:
Объем исходных файлов: <объем до сжатия> байт(а)
Объем сжатых файлов: <объем после сжатия> байт(а)
Примечание 1. Вывод на примере архива test.zip из конспекта:
Объем исходных файлов: 7810260 байт(а)
Объем сжатых файлов: 7798267 байт(а)
"""
from zipfile import ZipFile

compressed_size = 0
file_size = 0
with ZipFile('files/workbook.zip') as zip_file:
    info = zip_file.infolist()
    for obj in info:
        compressed_size += obj.compress_size
        file_size += obj.file_size

print(f'Объем исходных файлов: {file_size} байт(а)')
print(f'Объем сжатых файлов: {compressed_size} байт(а)')
