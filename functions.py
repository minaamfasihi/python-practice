# def means you are going to create a function

# docstring is what you see when you do a help on a function
def my_add_func(arg1, arg2):
    """
    Here is my docstring
    :param arg1:
    :param arg2:
    :return:
    """
    print(arg1 + arg2)

my_add_func(1, 2)


def say_hello(name):
    print('hello ' + name)

say_hello('Minaam')

def add_num(num1, num2):
    return num1 + num2

x = add_num(1, 4)
print(x) # output: 5

print(add_num('one', 'two')) # output: 'onetwo'

def is_prime(num):
    """
    This function checks for a prime number
    :param n:
    :return:
    """
    for n in range(2, num):
        if num % n == 0:
            print('Not prime')
            break
    else:
        print('Number is prime')

is_prime(12)