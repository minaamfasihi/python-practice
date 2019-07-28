# combines the elements from two lists one by one

a = [1, 2, 3]
b = [4, 5, 6]

print(list(zip(a, b))) # [(1, 4), (2, 5), (3, 6)]

for pair in zip(a, b):
    print(max(pair))

print(list(map(lambda pair: max(pair), zip(a, b)))) # [4, 5, 6]

x = [1, 2, 3]
y = [4, 5, 6, 7, 8]
print(list(zip(x, y))) # [(1, 4), (2, 5), (3, 6)]

d1 = {'a': 1, 'b': 2}
d2 = {'c': 4, 'd': 5}

print(list(zip(d1, d2))) # [('a', 'c'), ('b', 'd')]

print(list(zip(d2, d1.values()))) # [('c', 1), ('d', 2)]

def switchKV(d1, d2):
    dout = {}
    for d1key, d2val in zip(d1, d2.values()):
        dout[d1key] = d2val

    return dout

print(switchKV(d1, d2)) # {'a' : 4, 'b' : 5}