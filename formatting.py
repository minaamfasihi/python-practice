x = 13.3

print('Place my variable here: %s' %(x)) # output: Place my variable here: 13.3

# The 1 in %1.2f tells the minimum number of digits that the result should contain

print('Floating point number: %1.2f' %(13.145)) # output: 13.14
print('Floating point number: %1.5f' %(13.145)) # output: 13.14500

# The number 6 in %6.2f pads the output with 6 digits at least if there are less numbers in the result
print('%6.2f' %(18.134))

# conversion to string
print('Convert to string %s' %(123))
print('Convert to string %r' %(123))

print('First: %s, Second: %s, Third: %s' %('hi', 'two', 3)) # output: First: hi, Second: two, Third: 3

print('First: %s, Second: %s' %(2, 2)) # output: First: 2, Second: 2

print('First: {x} Second: {x}'.format(x = 'inserted')) # output: First: inserted Second: inserted

# output: First: inserted Second: two! Third: inserted
print('First: {x} Second: {y} Third: {x}'.format(x = 'inserted', y = 'two!'))

