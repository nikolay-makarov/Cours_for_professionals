"""
Средняя зарплата
Вам доступен файл salary_data.csv, который содержит анонимную информацию о зарплатах сотрудников в различных компаниях.
В первом столбце записано название компании, а во втором — зарплата очередного сотрудника:
company_name;salary
Atos;135000
ХайТэк;24400
Philax;128600
Инлайн Груп;43900
IBS;70600
Oracle;131600
Atos;91000
...
Напишите программу, которая упорядочивает компании по возрастанию средней зарплаты ее сотрудников и выводит их названия,
каждое на отдельной строке.
Если две компании имеют одинаковые средние зарплаты, они должны быть расположены в лексикографическом порядке
их названий.
Примечание 1. Средняя зарплата компании определяется как отношение суммы всех зарплат к их количеству.
Примечание 2. Разделителем в файле salary_data.csv является точка с запятой, при этом кавычки не используются.
Примечание 4. Начальная часть ответа выглядит так:
Информзащита
Форс
OFT group
...
"""
import csv
import statistics

with open('salary_data.csv', 'r', encoding='utf-8') as file:
    data = csv.DictReader(file, delimiter=';')
    company_salary_dict = {}
    # Создаем словарь, в который в качестве ключей помещаем названия компаний,
    # в качестве значений списки с зарплатами
    for row in data:
        company_salary_dict.setdefault(row['company_name'], []).append(int(row['salary']))
result = sorted(company_salary_dict, key=lambda item: statistics.mean(company_salary_dict[item]))
print(*result, sep='\n')