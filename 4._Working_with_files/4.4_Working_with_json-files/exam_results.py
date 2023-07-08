"""Результаты экзамена 🌶️
Вам доступен файл exam_results.csv, который содержит информацию о прошедшем экзамене в некотором учебном заведении.
В первом столбце записано имя студента, во втором — фамилия, в третьем — оценка за экзамен, в четвертом —
дата и время сдачи в формате YYYY-MM-DD HH:MM:SS, в пятом — адрес электронной почты:
name,surname,score,date_and_time,email
Jayson,Edwards,2,2021-11-10 10:00:00,sonnen@yahoo.com
April,Sims,3,2021-11-01 11:00:00,retoh@outlook.com
...
Каждый студент имеет право пересдать экзамен два раза, поэтому он может встречаться в исходном файле до трёх раз
с различной оценкой и различными датой и временем сдачи.
Напишите программу, которая для каждого студента определяет его максимальную оценку, а также дату и время ее получения.
Программа должна создать список словарей, каждый из которых содержит следующие пары ключ-значение:
    name — имя студента
    surname — фамилия студента
    best_score — максимальная оценка за экзамен
    date_and_time — дата и время получения максимальной оценки в исходном формате
    email — адрес электронной почты
Полученный список программа должна записать в файл best_scores.json, причем словари в списке должны быть расположены
в лексикографическом порядке названий электронных почт.
Примечание 1. Если при пересдаче студент получил такую же оценку, что и в прошлый раз,
то в качестве даты следует указать дату пересдачи.
"""
import csv
import json
from datetime import datetime


with open('exam_results.csv', 'r', encoding='utf-8') as file:
    data = csv.DictReader(file, fieldnames=['name', 'surname', 'best_score', 'date_and_time', 'email'])
    next(data)
    result = [{}]
    for elem in sorted(data,
                       key=lambda x: (x['email'],
                                      x['best_score'],
                                      datetime.strptime(x['date_and_time'].strip(), '%Y-%m-%d %H:%M:%S'))):
        if result[-1].get('email') == elem['email']:
            result.pop()
        elem['best_score'] = int(elem['best_score'])
        result.append(elem)

with open('best_scores.json', 'w', encoding='utf-8') as out_file:
    json.dump(result[1:], out_file, indent=3)
