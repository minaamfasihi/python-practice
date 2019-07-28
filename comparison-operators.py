# == if the two values are equal
print(3 == 3) # output: true

# != is the same as <>
print(1 != 2) # output: true
# print(1 <> 2) # output: true but this is deprecated now

# chained comparison operators

# this is similar to ANDing
print(1 < 2 < 3) # output: true

if 1 < 2 and 2 < 3:
    print("hello")

print(1 < 3 > 2) # output: true

if 1 == 2 or 1 < 2:
    print('yayyyy')
