def ran_check(num, low, high):
    # Check if a num is between high and low
    if num in range(low, high):
        print("%s is in the range" %str(num))
    else:
        print("Outside the range")

def ran_bool(num, low, high):
    return num in range(low, high)

print(ran_bool(5, 1, 10))

def up_low(str):
    d = {'upper': 0, 'lower': 0}
    for c in str:
        if c.isupper():
            d['upper'] += 1
        elif c.islower():
            d['lower'] += 1
        else:
            pass

    print("Upper case: ", d['upper'])
    print("Lower case: ", d['lower'])

up_low("Minaam")

def uniquify_list(l):
    x = []
    for item in l:
        if item not in x:
            x.append(item)

    return x

print(uniquify_list([1, 2, 3, 4, 1, 2, 3, 9]))

def multiply_all(l):
    x = 1
    for a in l:
        x *= a
    return x

print(multiply_all([1, 2, 3, 4, 5]))

def is_palindrome(str):
    return str == str[::-1]

print(is_palindrome("ABAA"))


# Pangrams are words or sentences containing every letter of the alphabet at least once.
import string
def is_pangram(str, alphabet = string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str.lower())

print(is_pangram("the quick brown fox jumps over the lazy dog"))