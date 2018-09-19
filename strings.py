# imports the print 'function' from python 3 into python 2
from __future__ import print_function

str = 'Hello world'
str2 = "I'm a good boy"
# \n prints a new line
str3 = "Here is a new line \n and here is the second"
# \t print a tab
str4 = "Here is a new line \t and here is the second"
print(str4)

print(len('Hello World')) # 11
s = 'Hello World'
# grab everything from the first index, : means onwards
print(s[1:]) # output: ello World
print(s) # output: Hello World (no change in the original string)

print(s[:3]) # output: Hel (grab everything upto index 3 (excluding index 3 itself)

print(s[:]) # output: Hello World (print everything)

print(s[-1]) # output: d (prints the last character)

print(s[-len(s)]) # output: H (first char)

print(s[:-1]) # output: print everything but the last char

print(s[::1]) #output: Hello World (print everything in step size of 1)

print(s[::2]) # output: HloWrd (print every other element in step size of 2)

print(s[::-1]) # output: dlroW oellH (print reverse of string)

# Strings are immutable, you cannot change them

# s[0] = 'A' # error

s = s + ' concatenate me!' # can concatenate to a string
print(s)

letter = 'z'
print(letter * 10) # prints z 10 times

print(s.upper()) # output: HELLO WORLD

print(s.lower())

s = "Hello"
print(s.split()) # output: prints Hello, no splitting

print(s.split('e')) # output: ['H', 'llo'] (splits around e)

