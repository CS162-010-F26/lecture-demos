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

# The call stack is the set of function calls' stack frames nested
# on top of each other that store function-local variables and parameters.
# Every function call gets its own stack frame in which to store its
# own local variables and parameters.

# It is possible if a function recurses too many times without popping
# stack frames off the stack, it can run out of space on the stack.
# This is known as a stack overflow.

# The call stack is often pretty small.

# In practice, stack overflows are impossible to recover from.
# So, Python prevents stack overflows caused by deep recursion by
# enforcing a "soft" recursion limit. If you exceed that limit,
# it raises a RecursionError. You can, by the way, raise the soft
# limit if you want.

# main() calls fib(100)
#            fib(99)             fib(98)
#         fib(98)   fib(97)    fib(97) fib(96)

# Two main speed-up techniques:
# 1. Memoization     (cache results)
# 2. Dynamic programming (CS 325 covers this)

def main() -> None:
    print(fib(100))

if __name__ == '__main__':
    main()
