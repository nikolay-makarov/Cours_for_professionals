"""Итератор Cycle
Реализуйте класс Cycle, порождающий итераторы, конструктор которого принимает один аргумент:
iterable — итерируемый объект
Итератор класса Cycle должен циклично генерировать последовательность элементов итерируемого объекта iterable.
Примечание 1. Гарантируется, что итерируемый объект, передаваемый в конструктор класса,
не является множеством и итератором.
Примечание 2. Элементы итерируемого объекта, генерируемые итератором, должны располагаться в своем изначальном порядке.
"""


class Cycle:
    def __init__(self, iterable: any) -> None:
        self.iterable: any = iterable
        self.length: int = len(iterable)
        self.index: int = -1

    def __iter__(self) -> 'Cycle':
        return self

    def __next__(self):
        self.index += 1
        return self.iterable[self.index % self.length]


cycle = Cycle(range(100_000_000))

print(next(cycle))
print(next(cycle))
