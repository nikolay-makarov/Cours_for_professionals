"""Бесплатные курсы берут свое 😢
Для дополнительного заработка Тимур решил заняться продажей овощей.
У него имеются данные о продажах за год, разделенные на четыре файла по кварталам:
quarter1.csv, quarter2.csv, quarter3.csv и quarter4.csv.
В каждом файле в первом столбце указывается название продукта,
а в последующих — количество проданного продукта в килограммах за определенный месяц:
продукт,январь,февраль,март
Картофель,39,61,3
Дайкон,51,96,83
...
Также присутствует файл prices.json, содержащий словарь, в котором ключом является название продукта,
а значением — цена за килограмм в рублях:
{
   "Картофель": 53,
   "Дайкон": 55,
...
}
Напишите программу, которая выводит единственное число — сумму, заработанную Тимуром за год на продаже овощей.
"""
import json
import csv
from collections import Counter

counter = Counter()
result = 0

for number in range(1, 5):
    with open(f'quarter{number}.csv', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            product, *amount = row
            counter.update({product: sum(map(int, amount))})

with open('prices.json', encoding='utf-8') as json_file:
    prices = json.load(json_file)

for product, amount in counter.items():
    result += prices[product] * amount

print(result)
