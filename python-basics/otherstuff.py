# Imports are used to import other code into your module / Python file.
# import math # Import the math package (whole-package import)
from math import pow, sqrt, sin as math_sin # individual object / function imports

def sin() -> None:
    print('Commits one of the deadly sins')

def change_me(x: int) -> None:
    x = 10

def print_list(the_list: list[str]) -> None:
    # In a function, if you modify an element within
    # a list parameter, that does actually modify the element
    # in the list that was passed as an argument.

    the_list[0] = 'first'

    for elem in the_list:
        print(elem)

def main() -> None:
    # Python's relational operators:
    # == (equality)
    # < (less than)
    # <= (less than or equal to)
    # > (greater than)
    # >= (greater than or equal to)
    # !=
    user_guess = int(input('Guess the magic number: '))
    magic_number = 7
    if not (user_guess < magic_number or user_guess > magic_number): # usually an expression of type bool
        # Body goes here. Indented.
        print('Good job!')

        # Nested if statement
        # if SOME_CONDITION:
            # another body goes here

        # If statements (and loops) do NOT get their own scopes
        # in Python.
        x = 'x'
    elif user_guess < magic_number and not (user_guess > magic_number):
        print('Too low!')
    else:
        # Body goes here. Indented
        print('Too high!')

    # print(x) # This works, but only if the user's guess was correct

    # Logical operators:
    # and, or, not
    # a and b: true if and only if both a and b are true
    # a or b: true if and only if at least one of a or b is true
    # not a: true if and only if a is false

    # Two kinds of loops in Python:
    # 1. While loops
    # 2. For loops

    # While loops are EXACTLY like if statements, except:
    while user_guess != magic_number:
        user_guess = int(input('Guess again: '))

    # For loops in Python are range-based.
    # An iterable is something that you can iterate over.
    # Like a list / array / dict / tuple / range / etc
    # Let's say SOME_ITERABLE is a list of integers: [1, 4, -2, 5]

    # A range is a special data type that represents a
    # sequence of numbers at a regular interval. Every range
    # has a start, a stop, and an end.
    # The start indicates the first number in the range.
    # The stop indicates the first number not in the range.
    # The step indicates the interval between numbers in the range.

    # To construct a range, use the range function:
    # range(start, stop, step)

    # range(1, 10, 2) is a range with the following numbers inside it:
    # [1, 3, 5, 7, 9]

    # range(2, 10, 2) is a range with the following numbers inside it:
    # [2, 4, 6, 8]
    for i in range(2, 10, 2):
        # Some body here
        print(i)
        
        # Inside a loop, you can use
        # break: stops the loop / jumps below the loop body
        # continue: jumps back to the condition evaluation / iterator update

        # Some people will tell you that break and continue
        # are bad practice.
        # if some_complicated_condition:
            # break

    print()

    # If you pass just one argument to range(), then it's the stop.
    # In that case, the start is implied to be 0, and the step
    # is implied to be 1.
    # [0-9]
    for i in range(10):
        print(f'{i+1}. hello')

    # If you pass two arguments to range(), then the first is the
    # start, the second is the stop, and the step is implied to be 1.
    # [1-6]
    for i in range(1, 7):
        print(f'{i+1}. goodbye')

    print('down here')

    # dot operator (.) reaches inside the thing on the left to
    # grab the thing on the right
    print(pow(2, 5))
    print(sqrt(100))
    print(pow(100, 0.5))

    # A list is an ordered sequence of values.
    # In Python, a List is a special data type that represents a list.
    # Technically, in Python, a List can be heterogeneous (more than
    # one data type). However, Mypy doesn't like that.
    # Mypy wants our lists to be homogeneous (everything is of the
    # same type)
    
    # To create a list:
    # my_list = [] # empty list, that's fine
    my_list = ['hello', 'world', '!', '']
    
    # Element: something inside something else

    # To access an element within a list:
    print(my_list[0]) # First element has an index of 0
    print(my_list[1]) # Second element has an index of 1
    # print(my_list[4]) # Raises an IndexError
    print(my_list[-1]) # This is the last element

    # To get the length of a list: len(my_list)
    print(len(my_list)) # Prints 4

    # You can iterate over a list. A list is an iterable.
    for word in my_list:
        print(word)

    # You can append elements to Lists in Python.
    # To append means to add to the end.
    my_list.append('goodbye')

    print(my_list[4]) # Prints goodbye

    # You can concatenate two lists using the + operator
    # my_list = my_list + ['hello', 'again']

    # You can delete elements from lists in Python
    del my_list[2]

    # ['hello', 'world', '', 'goodbye']

    # You can insert elements into the middle of a list
    my_list.insert(1, 'Harry Potter')

    # ['hello', 'Harry Potter', 'world', '', 'goodbye']
    
    print_list(my_list)

    print(my_list[0]) # Prints first

    x = 1
    change_me(x) # This does NOT change x!!! x is still 1

    # print(int('hello')) # This raises a ValueError. Program will crash.
    
    # When a program crashes due to an uncaught exception, it automatically
    # prints a traceback to the terminal.

    my_cool_variable: float = 1
    my_cool_variable = 3.14




if __name__ == '__main__':
    main()
