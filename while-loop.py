x = 0
while x < 10:
    x += 1
    print('HI')

else:
    print('All Done') # output: All Done (after the while loop)

# Break, Continue, Pass

# Break: breaks out of the current closest enclosing loop
# Continue: goes to the top of the closest enclosing loop
# Pass: does nothing

x = 0
while x < 10:
    x += 1
    print(x)
    if x == 3:
        print('x equals 3')
        break
    else:
        print('continuing')
        continue