"""
Популярные домены
Вам доступен файл data.csv, который содержит неповторяющиеся данные о пользователях некоторого ресурса.
В первом столбце записано имя пользователя, во втором — фамилия, в третьем — адрес электронной почты:
first_name,surname,email
John,Wilson,johnwilson@outlook.com
Mary,Wilson,marywilson@list.ru
...
Напишите программу, которая создает файл domain_usage.csv, имеющий следующее содержание:
domain,count
rambler.ru,24
iCloud.com,29
...
где в первом столбце записано название почтового домена, а во втором — количество пользователей,
использующих данный домен. Домены в файле должны быть расположены в порядке возрастания количества их использований,
при совпадении количества использований — в лексикографическом порядке.
Примечание 1. Разделителем в файле data.csv является запятая, при этом кавычки не используются.
Примечание 2. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
Примечание 3. Начальная часть файла domain_usage.csv выглядит так:
domain,count
rambler.ru,24
iCloud.com,29
...
Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.
"""
import csv

with open('data.csv', encoding='utf-8-sig', newline='') as file:
    reader = csv.DictReader(file)
    domains_dict = {}
    for row in reader:
        domain = row['email'].split('@')[1]
        domains_dict[domain] = domains_dict.get(domain, 0) + 1

with open('domain_usage.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['domain', 'count'])
    sorted_list = sorted(domains_dict.items(), key=lambda x: (x[1], x[0]))
    writer.writerows(sorted_list)
