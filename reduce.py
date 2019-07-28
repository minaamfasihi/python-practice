# reduce(function, sequence)
# Continually applies the function to the sequence in such a way that the result of applying on first two elements
# is carried forward and used with the third element and so on.

from functools import reduce
lst = [47, 11, 42, 13]
print(reduce(lambda x, y: x + y, lst)) # 113
# 47 + 11 = 58, 58 + 42 = 100, 100 + 13 = 113

max_find = lambda a, b: a if a > b else b

print(reduce(max_find, lst)) # finds the maximum in the list