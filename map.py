def fahrenheit(T):
    return ((9.0 / 5) * T + 32)

print(fahrenheit(12))

# we can use map to apply the fahrenheit function to every member of that object

temp = [0, 22.5, 40, 100]
map(fahrenheit, temp) # this applies the fahrenheit function to every item in temp

map(lambda T: (9.0 / 5) * T + 32, temp) # this will achieve the same as above

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
# in python 3, map function returns iterators, so we need to cast it to list
map(lambda x, y, z: list(x + y + z), a, b, c)
