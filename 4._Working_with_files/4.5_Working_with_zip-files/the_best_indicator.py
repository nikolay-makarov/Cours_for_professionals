"""Наилучший показатель
Вам доступен архив workbook.zip, содержащий различные папки и файлы.
Напишите программу, которая выводит название файла из этого архива, который имеет наилучший показатель степени сжатия.
Примечание 1. Если файл находится в папке, вывести следует только название без пути.
Примечание 2. Гарантируется, что в исходном архиве только один файл имеет наилучший показатель степени сжатия.
Примечание 3. Степень сжатия файла характеризуется коэффициентом K,
определяемым как отношение объема сжатого файла Vc к объему исходного файла Vo, выраженным в процентах:
K=Vc/Vo⋅100%
"""
from zipfile import ZipFile

with ZipFile('files/workbook.zip') as zip_file:
    print(
        min(
            filter(
                lambda val:
                val.file_size,
                zip_file.infolist()
            ),
            key=lambda x: x.compress_size / x.file_size
        ).filename.split('/')[-1]
    )