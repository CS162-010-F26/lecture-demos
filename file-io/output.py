from typing import TextIO

def write_data_to_file(f: TextIO) -> None:
    # To write data to the terminal (standard output), we use print()
    
    # To write data to a TextIO file variable, we use the .write() method

    # Escape sequences are special character sequences that you can write
    # inside a string literal that get reinterpreted / expanded into
    # something else, usually a special character.
    # \n (newline character sequence)
    # \t (tab)
    # \\ (backslash escape sequence)
    f.write('Hello, World!\n')
    f.write('Hello, World!\n')

def main() -> None:
    # File output is like "saving".
    
    # w is for writing in truncate mode. To truncate means to remove
    # everything.
    # a is for writing in append mode. Adds on to the end of the file.
    with open('out.txt', 'a') as output_file:
        # Context manager body
        write_data_to_file(output_file)

if __name__ == '__main__':
    main()
