import math

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
    # // (integer division)
    # % (modulo operator): remainder after division
    # **
    
    print(10 % 3) # Prints 1 
    print(math.pow(2, 5)) # Prints 32
    
    print((7 + 2) * 3)

    # Suppose you want to create a variable and store a value inside it
    # = is the assignment operator.
    # 1. Computes the value on the right
    # 2. Stores that computed value in the variable on the left
    #     (loosely)
    # An identifier is a name. Identifiers can contain numbers, letters,
    # and underscores, but they must start with a letter or underscore
    xyz = 15 + 2


if __name__ == '__main__':
    main()
