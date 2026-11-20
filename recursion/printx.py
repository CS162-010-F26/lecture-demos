

# Write a function called print_x(height, indentation)
# that prints a big X out of asterisks to the terminal with the given
# height (assume height is odd) and indentation

# print_x(5, 1):
# *   *
#  * *
#   *
#  * *
# *   *
def print_x(height: int, padding: int) -> None:
    if height % 2 == 0 or height < 1 or padding < 0:
        raise ValueError('Error: bad arguments')

    # Base case
    if height == 1:
        for _ in range(padding):
            print(' ', end='')
        print('*')
        return
    
    for _ in range(padding):
        print(' ', end='')
    print('*', end='')
    for _ in range(height - 2):
        print(' ', end='')
    print('*')

    print_x(height - 2, padding + 1)

    for _ in range(padding):
        print(' ', end='')
    print('*', end='')
    for _ in range(height - 2):
        print(' ', end='')
    print('*')


def main() -> None:
    print_x(7, 0)

    print()
    print_x(13, 1)

if __name__ == '__main__':
    main()
