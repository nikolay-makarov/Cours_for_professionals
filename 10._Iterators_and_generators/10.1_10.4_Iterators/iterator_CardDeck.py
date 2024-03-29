"""Итератор CardDeck
Реализуйте класс CardDeck, порождающий итераторы, конструктор которого не принимает никаких аргументов.
Итератор класса CardDeck должен генерировать последовательность из 5252 игральных карт,
а после возбуждать исключение StopIteration. Каждая карта должна представлять собой строку в следующем формате:
<номинал> <масть>
Например, 7 пик, валет треф, дама бубен, король червей, туз пик.
Примечание 1. Карты, генерируемые итератором, должны располагаться сначала по величине номинала, затем масти.
Примечание 2. Старшинство мастей по возрастанию: пики, трефы, бубны, червы. Старшинство карт в масти по возрастанию:
двойка, тройка, четверка, пятерка, шестерка, семерка, восьмерка, девятка, десятка, валет, дама, король, туз.
Примечание 3. Масти не требуют склонения и независимо от номинала должны сохранять следующее написание:
пик, треф, бубен, червей.
"""


class CardDeck:
    SUITS: tuple[str] = ('пик', 'треф', 'бубен', 'червей')
    VALUES: tuple[str] = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз')

    def __init__(self) -> None:
        self.n = -1

    def __iter__(self) -> 'CardDeck':
        return self

    def __next__(self) -> str:
        self.n += 1
        if self.n >= 52:
            raise StopIteration
        return f'{CardDeck.VALUES[self.n % 13]} {CardDeck.SUITS[self.n // 13]}'


cards = list(CardDeck())

print(cards[9])
print(cards[23])
print(cards[37])
print(cards[51])
