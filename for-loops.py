l = [1, 2, 3, 4, 5]
for item in l:
    if item % 2 == 0:
        print('even')
    else:
        print('odd')

list_sum = 0
for item in l:
    list_sum += item

print(list_sum)

sentence = 'this is a string'
for letter in sentence:
    print(letter)

tup = (1,2,3,4,5)
for item in tup:
    print(item)

l = [(2, 4), (6, 8), (10, 12)]
print(l[2][0]) # output: 10

for tup in l:
    print(tup) # output: (2, 4) (6, 8) (10, 12)

# tuple unpacking
for (t1, t2) in l:
    print(t1) # output: 2, 6, 10
    print(t2) # output: 4, 8, 12

for (t1, t2) in l:
    print(t1 + t2) # output: 6, 14, 22

d = {'k1': 1, 'k2': 2, 'k3': 3}
for item in d:
    print(item) # output: k1, k2, k3 (only keys)

# in Python 3, you do d.items() to iterate over a dictionary
# in Python 2, you do d.iteritems() to iterate over a dictionary

for k, v in d.items():
    print(k) # key
    print(v) # value

for k, v in d.iteritems():
    print(k)
    print(v)

# same as above, parenthesis in (3, 4) doesnt matter
for (k, v) in d.iteritems():
    print(k)
    print(v)