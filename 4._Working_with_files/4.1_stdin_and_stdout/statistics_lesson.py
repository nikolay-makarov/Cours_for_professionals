"""
Урок статистики
Дан список чисел, каждое из которых — рост очередного ученика онлайн-школы BEEGEEK.
Напишите программу, которая определяет рост самого низкого и самого высокого учеников,
а также средний рост среди всех учеников.
Формат входных данных
На вход программе подается произвольное количество строк, в каждой строке записано натуральное число —
рост очередного ученика онлайн-школы BEEGEEK.
Формат выходных данных
Программа должна определить рост самого низкого и самого высокого учеников,
а также средний рост среди всех учеников.
Полученные результаты должны быть выведены в следующем формате:
Рост самого низкого ученика: <рост самого низкого ученика>
Рост самого высокого ученика: <рост самого высокого ученика>
Средний рост: <средний рост среди всех учеников>
Примечание 1. Если на вход программе ничего не подается, то она должна выводить текст нет учеников.
"""
import sys, statistics

measurement = [int(number) for number in sys.stdin]
if measurement:
    print(f'Рост самого низкого ученика: {min(measurement)}')
    print(f'Рост самого высокого ученика: {max(measurement)}')
    print(f'Средний рост: {statistics.mean(measurement)}')
else:
    print('нет учеников')
