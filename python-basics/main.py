import math

# This is global scope here.
# This is a global variable
# You SHOULD NOT use global variables as a communication
# channel between functions.
z: int = 0

# In the parentheses, you put parameters
#    (placeholders for the values the function takes as inputs)
# After parentheses, you do -> return_type
#    (the type of the value that replaces the function call)
def add(x: float, y: float) -> float: # This is the function header
    # Function body, dictated by indentation
    z = x + y
    return z
    print('hello') # This is dead code

def print_hello() -> None:
    print('Hello')

def main() -> None:
    # The print function takes in some inputs,
    # converts them into a string, and writes that
    # string to standard output.

    # Standard output is a special file stream that
    # every process has. In most cases, by default,
    # a process's standard output is hooked up to
    # the terminal.

    # A process is a running instance of a program.
    print("Hello, \"World\"!")

    # Python has various built-in "primitive" types
    # of data.
    
    # A literal is a hardcoded value

    # str: string (a sequence of characters)
    # int: integer (whole number)
    #       1, -1, -1000000, 
    # float: floating point number (a number with a decimal point somewhere)
    #       3.14, -3.14, 3., .3
    # bool: boolean (True/False)
    #       True, False
    
    # An expression is a piece of code with a type and a value
    # Arithmetic operators combine numeric expressions to produce bigger,
    # more complicated numeric expressions
    print(1 + 7.3)

    # Arithmetic operators:
    # +
    # -
    # *
    # /
    # // (integer division (floor division))
    # % (modulo operator): remainder after division
    # **
    
    print(10 % 3) # Prints 1
    print(math.pow(2, 5)) # Prints 32. Less confusing to Mypy than 2 ** 5.
    
    print((7 + 2) * 3)

    # Suppose you want to create a variable and store a value inside it.
    # = is the assignment operator.
    # 1. Computes the value on the right
    # 2. Stores that computed value in the variable on the left
    #     (loosely)
    # An identifier is a name. Identifiers can contain numbers, letters,
    # and underscores, but they must start with a letter or underscore
    xyz: int = 15 + 2

    # You can now use your variable as an expression.
    print(xyz) # Prints 17
    print(type(xyz))

    # xyz = 'hello' # The interpreter is okay with this, Mypy is not

    #print(xyz) # Prints hello
    #print(type(xyz))

    # Mypy is a static analysis tool, specifically a type checker.
    
    x = 2
    x = x + 1 # x is now 3
    x += 1 # This is shorthand for the above
    x -= 2 # x is now 2 again!
    x *= 4 # x is now 8
    print(x)

    print(f'The value of x is {x}')

    # (Explicit) type casting in Python:
    x_as_a_string = str(x)
    # I think you can type cast any primitive type
    # into any other primitive type
    
    # You can also cast strings to ints
    favorite_number = '27'
    print(int(favorite_number) * 2) # Prints 54 

    # It only works if the string stores a valid integer value
    #favorite_number = 'hello'
    #print(int(favorite_number) * 2) # Value Error
    # MyPy doesn't catch the above error, but the program crashes
    # at runtime due to the exception

    # To call a function, you write its name, then parentheses,
    # then ARGUMENTS in the parentheses
    two_plus_nine = add(2.0, 9.0)
    print(two_plus_nine)
    print(add(2.0, 9.0))

    print_hello()

    # A scope is a region of code in which a symbol is accessible.
    # A symbol is a named thing. (variables, functions)

    # In Python, there are three kinds of scopes:
    # 1. Global scope (module scope). Unindented scope.
    # 2. Function-local scope. This is simply the scope in a function.
    #       In Python, every function gets its own scope.
    # 3. Class scope

    # When you define a symbol, the scope in which you defined it
    # is the scope in which it's accessible

    # Scopes can exist inside other scopes.
    # In an inner scope, you can define symbols that are already
    # defined in the outer scope.
    #z = 3.14 # This is called shadowing
    #print(z) # This prints 3.14
    #z = 7.1

    

if __name__ == '__main__':
    main()
