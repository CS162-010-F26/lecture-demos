def main() -> None:
    # Every process also has a special file stream called
    # standard input. By default, if you're running the
    # program as a foreground process in a terminal, then
    # the standard input stream is usually hooked up to
    # the terminal.

    # The difference is in direction.

    # If you want to write a program that asks the user
    # a question, and reads their answer, and stores it
    # in a variable, you might use standard input for that.
    
    age = int(input('How old are you?: '))
    print(f'Oh, I see, so you\'re {age} years old.')

if __name__ == '__main__':
    main()
