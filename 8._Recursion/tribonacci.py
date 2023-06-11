"""Функция tribonacci()
Последовательность Трибоначчи – последовательность натуральных чисел,
где каждое последующее число является суммой трех предыдущих:
1, 1, 1, 3, 5, 9, 17, 31, 57, 105 …
Реализуйте функцию tribonacci() с использованием рекурсии и мемоизации, которая принимает один аргумент:
    n — натуральное число
Функция должна возвращать n-й член последовательности Трибоначчи.
"""


def tribonacci(n: int) -> int:
    cache: dict = {1: 1, 2: 1, 3: 1}

    def recursion(number: int = n) -> int:
        if number <= 3:
            return 1
        result = cache.get(number)
        if not result:
            cache[number] = recursion(number - 1) + recursion(number - 2) + recursion(number - 3)
            return cache[number]
        return result

    return recursion()


print(tribonacci(1))
print(tribonacci(7))
print(tribonacci(4))
