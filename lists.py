my_list = [1, 2, 3]
my_list = ['string', 23, 1.2, 'o']

print(len(my_list)) # output: 4

my_list = ['one', 'two', 'three', 4.5]
print(my_list[1:]) # output: ['two', 'three', 4.5]

print(my_list[:3]) # ['one', 'two', 'three']

print(my_list + ['new item']) # output: ['one', 'two', 'three', 4.5, 'new item']
# original list remains unmodified

print(my_list * 2) # output: ['one', 'two', 'three', 4.5, 'one', 'two', 'three', 4.5]

l = [1, 2, 3]
l.append('append me!')
print(l) # output: [1, 2, 3, 'append me!']

print(l.pop()) # output: 'append me'
# by default pop, removes and returns the last element. you can provide the index too

print(l.pop(1)) # output: 2

# print(l[99]) # error

new_list = ['a', 'e', 'x', 'b', 'c']
new_list.reverse()
print(new_list) # output: ['c', 'b', 'x', 'e', 'a']
new_list.sort()
print(new_list) # output: ['a', 'e', 'x', 'b', 'c']

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [7, 8, 9]
matrix = [l1, l2, l3]
print(matrix[0][1]) # output: 2

first_col = [row[0] for row in matrix] # for every row, grab its first element. Output: [1, 4, 7]