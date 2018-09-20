# 0 upto 10 (but not including)
x = range(0, 10)
# range(0, 10) is the same as range(10)
start = 5
stop = 20
for i in range(start, stop):
    print(i) # output: from 5 upto 20

for i in range(start, stop, 2): # 3rd argument is the step size
    print(i) # output: all the odd numbers from 5 uptil 20

# range vs xrange

# what if you want to iterate over a billion numbers? do you keep all of them in memory?
# that's where generators come into play. python 3's range function behaves as a generator by default.
# in python 2, you need to do xrange()
# recommended to use xrange in python 2 because the range function will save all the numbers in memory
# in list

# range() in python 2 returned a list
# e.g. x = range(1, 5)
# x would be: [1, 2, 3, 4]
# but since range in python 3 is a generator, we just get
# e.g. x = range(1, 4)
# type(x) # output: range (and not [1, 2, 3])

# Generator: A generator allows the generation of 'generated' objects
# that are provided at that instance but does not store every instance generated into memory
# this means a generator would not create a list to generate like range() does, but instead provide
# a one time generation of the numbers in that range
