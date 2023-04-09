"""Разные типы
Вам доступен файл data.json, содержащий список различных объектов:
[
   "nwkWXma",
   null,
   {
      "ISgHT": "dIUbf"
   },
   "Pzt",
   "BXcbGVTE",
   ...
]
Напишите программу, которая создает список, элементами которого являются объекты из списка,
содержащегося в файле data.json, измененные по следующим правилам:
- если объект является строкой, в его конец добавляется восклицательный знак;
- если объект является числом, он увеличивается на единицу;
- если объект является логическое значением, он инвертируется;
- если объект является списком, он удваивается;
- если объект является JSON-объектом (словарем), в него добавляется новая пара "newkey": null;
- если объект является пустым значением (null), он не добавляется.
Полученный список программа должна записать в файл updated_data.json.
Примечание 1. Например, если бы файл data.json имел вид:
["Hello", 179, true, null, [1, 2, 3], {"key": "value"}]
то программа должна была бы создать файл updated_data.json со следующим содержанием:
["Hello!", 180, false, [1, 2, 3, 1, 2, 3], {"key": "value", "newkey": null}]
"""
import json

with open('data.json', 'r', encoding='utf-8') as source:
    data = json.load(source)

result = []
for obj in data:
    match obj:
        case bool(obj):
            result.append(not obj)
        case list(obj):
            result.append(obj * 2)
        case str(obj):
            result.append(obj + '!')
        case dict(obj):
            obj['newkey'] = None
            result.append(obj)
        case int(obj) | float(obj):
            result.append(obj + 1)

with open('updated_data.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, indent=4)
