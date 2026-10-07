def c() -> None:
    print(int('hello')) # Raises a ValueError

    # The interpreter asks, "Can this function
    # handle the ValueError?"

    # If the answer is yes, then it handles the
    # ValueError and continues.

    # If the answer is no, then the current
    # function call TERMINATES.

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

def main() -> None:
    try:
        # try body
        x = a() # raising an exception does NOT return a value.
        # so the assignment operator does not execute.
        # so x is not defined.
    except ValueError: # This except block can catch ANY kind of exception
        # except body (error-handling code)
        print('Error: cannot cast given string value to integer')
    except IndexError:
        print('An index error occurred!')

    # print(x)

    # A ValueError is a kind of Exception.
    # Exception is a broad kind of data type.

    # Exceptions can be raised. To raise an exception basically
    # just means to generate it.

    # As a program is running, if at any point an exception is
    # raised, then the control flow changes.

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
