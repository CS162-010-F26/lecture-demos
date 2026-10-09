# from typing import TextIO
import typing

def read_file(the_file: typing.TextIO) -> None:
    for line in the_file:
        # Good idea: remove the \n from the end of the line variable:
        line = line.strip()
        
        # We can split a string into a list of smaller strings
        # by a token separator using .split()
        tokens = line.split(',')


def main() -> None:
    # File I/O stands for file input/output. (basically, saving and loading).
    
    # print() writes data to standard output, usually hooked up to
    # the terminal.

    # input() reads data from standard input, usually hooked up to
    # the terminal.

    # File input: reading data from a file.

    # 'r': reading
    # 'w': writing in truncate mode
    # 'a': writing in append mode
    with open('data.csv', 'r') as cool_reading_file:
        # context manager body goes here
        
        # cool_reading_file is an Iterable. You can iterate over it
        # in a for loop.
        read_file(cool_reading_file)

        # You can only use the file variable (cool_reading_file)
        # within the context manager body

    # cool_reading_file technically still exists, but you cannot really
    # use it

if __name__ == '__main__':
    main()
