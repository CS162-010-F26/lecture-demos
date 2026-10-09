from traceback import print_exc

def c() -> None:
    print(int('hello')) # Raises a ValueError

    # The interpreter asks, "Can this function
    # handle the ValueError?"

    # If the answer is yes, then it handles the
    # ValueError and continues.

    # If the answer is no, then the current
    # function call TERMINATES, and the exception
    # propagates down the call stack.

    # Remember: the call stack is the function calls that
    # are currently happening that led to this point.

def b() -> None:
    c()

    # The interpreter asks, "Can this function
    # handle the ValueError?"

    # If the answer is yes, then it handles the
    # ValueError and continues.

    # If the answer is no, then the current
    # function call TERMINATES.

def a() -> int:
    b()
    return 1

    # The interpreter asks, "Can this function
    # handle the ValueError?"

    # If the answer is yes, then it handles the
    # ValueError and continues.

    # If the answer is no, then the current
    # function call TERMINATES.

def get_age(name: str) -> int:
    if name == 'Alex':
        return 27
    elif name == 'Roger':
        return 30
    else:
        # We want to communicate that a bad value was passed
        # to this function
        raise ValueError(f'Bad value {name} passed to get_age()')


def main() -> None:
    try:
        # try body
        x = a() # raising an exception does NOT return a value.
        # so the assignment operator does not execute.
        # so x is not defined.
    except ValueError as ex: # This except block can catch ANY kind of exception
        # except body (error-handling code)
        print('Error: cannot cast given string value to integer')
        print(ex) # Prints error message stored within exception
        # print_exc()
    except IndexError as ex:
        print('An index error occurred!')
        print(ex)

    # print(x)

    # A ValueError is a kind of Exception.
    # Exception is a broad kind of data type.

    # Exceptions can be raised. To raise an exception basically
    # just means to generate it.

    # As a program is running, if at any point an exception is
    # raised, then the control flow changes.

    print(get_age('Alex'))
    print(get_age('Roger'))
    try:
        print(get_age('Jessica'))
    except ValueError as my_cool_exception:
        print(my_cool_exception)

    valid_input = False
    while not valid_input:
        valid_input = True
        try:
            age = int(input('What is your age?: '))

            if age < 0:
                valid_input = False
        except:
            valid_input = False

    print(age + 3)

if __name__ == '__main__':
    main()
