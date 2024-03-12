# Itertools: Products, Permutations, Combinations, Accumulate
from itertools import permutations
from functools import reduce

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


# lambda Inside the Another Function
def myfunc(n):
    # Lambda Inside the another function
    return lambda x: x * n


data = myfunc(2)
print(data(3))

# Use lambda for a map function
# map(func, seq)
a = [1, 2, 3, 4, 5, 6]
b = list(map(lambda x: x * 2, a))
print(b)

# Use filter for the filter function
arr = [12, 13, 14, 15, 16]
b = list(filter(lambda x: x % 2 == 0, arr))
print(b)

# Use reduce function to reduce the array into a single value


c = reduce(lambda x, y: x + y, arr)
print(c)
