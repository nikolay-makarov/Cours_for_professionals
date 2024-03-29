"""Функция around()
Реализуйте генераторную функцию, которая принимает один аргумент:
iterable — итерируемый объект
Функция должна возвращать генератор, порождающий последовательность кортежей, каждый из которых содержит
очередной элемент итерируемого объекта iterable, а также предыдущий и следующий за ним элементы:
(<предыдущий элемент>, <очередной элемент>, <следующий элемент>)
Для первого элемента предыдущим считается значение None, для последнего элемента следующим считается
так же значение None.
Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны располагаться
в своем исходном порядке.
Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
"""


def around(iterable):
    if iterable:
        iterator = iter(iterable)
        a = None
        b = next(iterator)
        yield from ((a, b, c, a := b, b := c)[:-2] for c in iterator)
        yield a, b, None


numbers = [1, 2, 3, 4, 5]
print(*around(numbers))

iterator = iter('hey')
print(*around(iterator))

print(list(around([])))