"""Функция card_deck()
Реализуйте генераторную функцию card_deck(), которая принимает один аргумент:
suit — одна из четырех карточных мастей: пик, треф, бубен, червей
Функция должна возвращать генератор, циклично порождающий колоду игральных карт без масти suit.
Каждая карта должна представлять собой строку в следующем формате:
<номинал> <масть>
Например, 7 пик, валет треф, дама бубен, король червей, туз пик.
Примечание 1. Карты, генерируемые итератором, должны располагаться сначала по величине номинала, затем масти.
Примечание 2. Старшинство мастей по возрастанию: пики, трефы, бубны, червы. Старшинство карт в масти по возрастанию:
двойка, тройка, четверка, пятерка, шестерка, семерка, восьмерка, девятка, десятка, валет, дама, король, туз.
Примечание 3. Масти не требуют склонения и независимо от номинала должны сохранять следующее написание:
пик, треф, бубен, червей.
"""


def card_deck(suit):
    suits = ['пик', 'треф', 'бубен', 'червей']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
    while True:
        for s in suits:
            if s != suit:
                for v in values:
                    yield f'{v} {s}'


generator = card_deck('пик')
cards = [next(generator) for _ in range(80)]
print(*cards)