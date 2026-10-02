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


    print(i)

    print('down here')

    # TODO explain range(10) and range(2, 10)



if __name__ == '__main__':
    main()
