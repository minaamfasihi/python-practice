# Integers and Floating point

# in Python 2, integer division is rounded off.
# in Python 3, you get true division
print(3/2) # 1.5 in Python 3
print(3.0/2) # for enforcing true division in Python 2, make one of the numbers a float
print(float(3)/2) # casting 3 to float
from __future__ import division # imports division module from python 3 into python 2

