def fib(x: int) -> int:
    # Trivial answers are given by base cases.
    # These are the base cases. Programmatically, base cases
    # are often just one or more if statements that handle
    # the smallest instances of the problem that you can imagine,
    # which don't require recursion because they're so small.
    if x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        # Intuition of recursion: In order to solve a large, complicated
        # instance of a problem, we break it down into potentially
        # multiple smaller / simpler instances of the same problem
        # until eventually, you're dealing with problem instances
        # that are so small / simple that their answers are trivial.
        return fib(x-1) + fib(x-2)

def main() -> None:
    print(fib(11)) # Prints 55

if __name__ == '__main__':
    main()
