"""Функция nonempty_lines()
Реализуйте генераторную функцию nonempty_lines(), которая принимает один аргумент:
file — название текстового файла, например, data.txt
Функция должна возвращать генератор, порождающий последовательность всех непустых строк файла file с
убранным символом переноса строки \n. Если строка содержит более 2525 символов, она заменяется многоточием ....
"""


def nonempty_lines(file):
    with open(file, 'r', encoding='utf-8') as file:
        yield from (line.rstrip() if len(line) < 26 else '...' for line in file if line != '\n')


lines = nonempty_lines('file1.txt')

print(next(lines))
print(next(lines))
print(next(lines))
print(next(lines))

