"""Итератор Alphabet 🌶️
Реализуйте класс Alphabet, порождающий итераторы, конструктор которого принимает один аргумент:
language — код языка: ru — русский, en — английский
Итератор класса Alphabet() должен циклично генерировать последовательность строчных букв:
русского алфавита, если language имеет значение ru
английского алфавита, если language имеет значение en
Примечание 1. Буква ё в русском алфавите не учитывается.
"""


class Alphabet:
    EN: list[int] = list(number for number in range(ord('a'), ord('z') + 1))
    RU: list[int] = list(number for number in range(ord('а'), ord('я') + 1))

    def __init__(self, language: str) -> None:
        self.lang: str = language
        self.index: int = -1

    def __iter__(self) -> 'Alphabet':
        return self

    def __next__(self) -> str:
        if self.lang == 'ru':
            alphabet_numbers = Alphabet.RU
            div = len(Alphabet.RU)
        else:
            alphabet_numbers = Alphabet.EN
            div = len(Alphabet.EN)
        self.index += 1
        return chr(alphabet_numbers[self.index % div])


en_alpha = Alphabet('en')

letters = [next(en_alpha) for _ in range(28)]
print(*letters)
