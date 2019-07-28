# lambda's body is a single expression, not a block of statements

# lambda's body is similar to what we would put in a def body's return statement. We simply type the
# result as an expression instead of explicitly returning it. Because it is limited to an expression, a
# lambda is less general than a def

# this works
# def square(num): return num ** 2

# syntax: lambda [input]: [output]
lambda num: num ** 2

# you can assign this to a label as well
square = lambda num: num ** 2
# usually we dont save the lambda functions since they are supposed to be anonymous
print(square(2))

even = lambda num: num % 2 == 0

print(even(2))

# grabs the first character of a string

first = lambda str: str[0]

print(first('Fasihi')) # output: F

rev = lambda str: str[::-1]
print(rev('Reversed')) # output: desreveR

adder = lambda x, y: x + y
print(adder(20, 90))