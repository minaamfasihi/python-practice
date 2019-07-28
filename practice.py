print('hello')
a = 1
print(type(a))
print(float(99) + 100)
print(10 / 2)
abc = '23'
print(type(int(abc)))
print(abc)
# name = input("Your name?")
# print("Welcome", name)

b = "as"
try:
    print(int(b))
except:
    print("Sorry")

for i in [4, 2, 5, 1]:
    print(i)

smallest = None # non-existence
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    # 'is' is stronger than equal in that it demands equality both in value and type. Implies "is the same as".
    # use 'is' only for booleans or None. Dont use it for numbers, floats or strings. There's also 'is not' operator
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print("After", smallest)

zot = 'abc'
# print(zot[5]) # error. Cant access beyond index 4.
print(len(zot))
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

# above loop can also be written as below. this is a definite loop.
fruit = 'banana'
for letter in fruit:
    print(letter)

# slicing
# s[0:4] # read as "s sub 0 through 4"
# second number is one beyond the end of the slice: 'up to but not including'
# if the second number is beyond the length of string, then it just prints uptil the end of string.
s = 'Monty Python'
print(s[0:4]) # Mont
print(s[6:7]) # P
print(s[6:20]) # Python
# if we leave off the first or last number of slice, it is assumed to be the beginning or end of string respectively.
print(s[:2]) # Mo
print(s[8:]) # thon
print(s[:]) # Monty Python
# when + is applied to strings, it means concatenation
a = 'Hello'
b = a + 'There'
print(b) # HelloThere

# using in as a logical operator
# the 'in' keyword can also be used to check to see if one string is in another string.
# the 'in' expression is a logical expression that returns True or False and can be used in an if statement.
fruit = 'banana'
print('n' in fruit) # true
print('m' in fruit) # false
if 'a' in fruit:
    print('Found it!')

# also works with arrays
print(1 in [1, 2, 3]) # true
# comparison on strings
if fruit == 'banana':
    print('All right, bananas')
# python has a number of string functions built into them. every string is an object and so it has methods.
# these functions dont modify the original string, instead they return a new string that has been altered.
greet = 'Hello Bob'
zap = greet.lower() # returns a new lowercase version of hello bob. returns a NEW string
print('Hi there'.lower())
stuff = 'Hello world'
print(type(stuff)) # <class 'str'>
print(dir(stuff)) # lists all the functions available on stuff
# Searching a string
# use find() to search for a substring within another string
# find() finds the first occurrence of the substring
# if the substring is not found(), find() returns -1
fruit = 'banana'
pos = fruit.find('na')
print(pos) # 2
aa = fruit.find('z') # -1
print(aa)
# search and replace
# the replace() functions is like a "search and replace" operation in a word processor
# it replaces all occurrences of the search string with the replacement string
greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')
print(nstr) # Hello Jane
nstr = greet.replace('o', 'X') # HellX BXb
print(nstr)

# stripping whitespace
# we want to remove whitespace at the beginning and/or end.
# lstrip() and rstrip() remove whitespace at the left or right
# strip() removes both beginning and ending whitespace
greet = '             Hello Bob'
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())

# prefixes
line = 'Please have a nice day'
print(line.startswith('Please')) # true
print(line.startswith('p')) # false

# getting university from an email address
data = 'From stephen.maquard@uct.ac.za Sat Jun 5 09:14:16 2009'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ', atpos) # look for space starting from the position of '@'
print(sppos)
host = data[atpos + 1 : sppos]
print(host)

# in python 3 all strings are unicode. python 3 natively understands non-latin character sets.
# in python 2, for chinese character, it might output str but if we prepend u and then write the char, then it will print the type to be
# type unicode whereas in python 3, it will still be type str
