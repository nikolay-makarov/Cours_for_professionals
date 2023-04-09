"""
Вам доступен файл countries.json, содержащий список JSON-объектов с
информацией о странах и исповедуемых в них религиях:
[
   {
      "country": "Afghanistan",
      "religion": "Islam"
   },
   {
      "country": "Albania",
      "religion": "Islam"
   },
   ...
]
Каждый объект из этого списка содержит два атрибута:
    country — страна
    religion — исповедуемая религия
Напишите программу, которая создает единственный JSON-объект, имеющий в качестве ключа название религии,
а в качестве значения — список стран, в которых исповедуется данная религия.
Полученный JSON-объект программа должна записать в файл religion.json.
Примечание 1. Страны в списках должны располагаться в своем исходном порядке.
Примечание 2. Начальная часть файла religion.json выглядит так:
{
   "Islam":[
      "Afghanistan",
      "Albania",
      "Algeria",
      ...
   ],
   ...
}
"""
import json

with open('countries.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

religions = {}
for item in data:
    religions.setdefault(item['religion'], []).append(item['country'])

with open('religion.json', 'w', encoding='utf-8') as out_file:
    json.dump(religions, out_file, indent=3)
