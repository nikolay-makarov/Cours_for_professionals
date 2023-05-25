from collections import ChainMap

empty_chain_map = ChainMap()
numbers = {'one': 1, 'two': 2}
letters = {'a': 'A', 'b': 'B'}

chain_map = ChainMap(numbers, letters)
print(empty_chain_map)
print(chain_map)
print(ChainMap.fromkeys([1, 2, 3], []))
