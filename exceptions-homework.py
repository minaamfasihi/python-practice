for i in ['a', 'b', 'c']:
    try:
        print(i ** 2)
    except:
        print('Cant multiply')

x = 5
y = 0
try:
    z = x / y
except:
    print('Seems like you got a 0')
finally:
    print('Finally coming out')

def ask():
    while True:
        try:
            a = int(input('Enter an int'))
        except:
            print('Incorrect input')
            continue
        else:
            print('Correct input')
            break
        finally:
            print('In finally')

ask()