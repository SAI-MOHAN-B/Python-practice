# Itertools: Products, Permutations, Combinations, Accumulate
from itertools import permutations

a = [1, 2, 3]
perm = permutations(a, 2)
print(list(perm))

# Lambda arguments: expressions
# variable = function
add5 = lambda a: a + 5
print(add5(5))

mul = lambda x, y: x * y
print(mul(2, 7))


def add_5_x(num):
    return num * 10


print(add_5_x(2))
