from __future__ import division # imports division module from python 3 into python 2
# after this, you can do true division

# Integers and Floating point

# in Python 2, integer division is rounded off.
# in Python 3, you get true division
print(3/2) # 1.5 in Python 3
print(3.0/2) # for enforcing true division in Python 2, make one of the numbers a float
print(float(3)/2) # casting 3 to float

# compute power
print(2**3)

# order of operations is multiplication first
print(2 + 10 * 10 + 3)

my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate
print(my_taxes)