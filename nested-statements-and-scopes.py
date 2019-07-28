# when you create a variable, it is stored in a namespace

# variables name also have a scope, the scope determines the visibility of that variable name
# to other parts of your code

x = 25

def printer():
    x = 50
    return x

print(x)
print(printer())

# name assignments will create or change local names by default

# name references search(at most) four scopes:
# these are:
 # 1) local
 # 2) enclosing functions
 # 3) global
 # 4) built-in

def greet():
    # Enclosing function
    name = 'Sammy'

    def hello():
        print('Hello ' + name)

    hello()

greet()

# scope of the variable is the block they are declared in starting from the point of definition of the name
# when you declare a variable inside a function, they are not related in any way to other variables
# with the same names used outside the function

x = 50
def func(x):
    print('x is ', x) # 50
    x = 2
    print('Changed local x to ', x) # 2

func(x)
print('x is still ', x) # 50


x = 50
def new_func():
    global x # this means that whenever I use x now, use the global x, not local
    print(x) # 50
    x = 2 # 2

print(x) # 50
new_func()
print(x) # 2