# applies the function to every element of sequence and returns that element only if that function
# returns true for that element

def even_check(num):
    if num % 2 == 0:
        return True
    return False

print(even_check(34))

lst = range(10)

# print(list(lst))

print(list(filter(even_check, lst))) # output: 0, 2, 4, 6, 8

print(list(filter(lambda a: a % 2 == 0, lst)))

print(list(filter(lambda num: num > 3, lst))) # 4, 5, 6, 7, 8, 9

