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

 