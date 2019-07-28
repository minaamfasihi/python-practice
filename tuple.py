t = (1, 'one')
print(len(t)) # output: 2
print(t[0]) # output: o
print(t[-1]) # output: 'one'

print(t.index('one')) # output: 0 (returns the index of that element in tuple)

print(t.count('one'))
# t[0] = 1 # error
l = [1, 2, 3]
l[0] = 100 # ok

# tuple has only count and index methods.
# use them only when you want your values to be immutable

