a = 2
b = 3

# the colon describes that there must be indentation afterwards
if a > b:
    print("true")
else:
    print('false')
# output: false

if True:
    print('Always runs')

loc = 'Bank'
if loc == 'Auto Shop':
    print('Welcome to auto shop')
elif loc == 'Bank':
    print('Welcome to bank')
else:
    print('Where are you?')