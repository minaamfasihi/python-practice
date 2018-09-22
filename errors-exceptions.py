try:
    2 + 's'
except TypeError: # you could also write 'except:'
    print('There was a type error')
finally:
    print('Finally this was printed')

try:
    f = open('testfile', 'w')
    f.write('Test write this')
except:
    print('Error in writing to file')
else:
    print('File write was a success') # this will print because at line 9, a new file will be created if one doesnt exist before

try:
    f = open('testfile123', 'r')
    f.write('Test write this')
except: # can also use: except IOError:
    print('Error in writing to file') # this is printed because file doesnt exist
else:
    print('File write was a success')
finally:
    print("Always executes")

# def ask_int():
#     try:
#         val = int(input('Please enter an integer: '))
#     except:
#         print('Looks like you did not enter an integer')
#     finally:
#         print('Finally block executed')
#
#     print(val)
#
# ask_int()

def robust_ask_int():
    while True:
        try:
            val = int(input('Please enter an int: '))
        except:
            print('Not an int, try again')
            continue
        else:
            print('An int indeed')
            break
        finally:
            print('Finally block executed')

        print(val)

robust_ask_int()