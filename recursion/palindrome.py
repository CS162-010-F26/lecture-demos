# Let's write a function that's given a string as an input
# and returns True if it's a palindrome, or False otherwise.
# We want to use recursion for this.

def is_palindrome(the_string: str) -> bool:
    # Intuition: Can we break this problem down into one or more smaller
    # instances of the same problem, then piece together the solution to
    # THIS instance?

    # Suppose we call is_palindrome('racecar'). racecar is quite a big string.
    # So maybe it's difficult to determine whether racecar is a palindrome.
    # But what if we could somehow, magically (i.e., via recursion), determine
    # if smaller, simpler strings are palindromes. How would we use that
    # magic to our advantage here?

    # A string is a palindrome if and only if:
    # 1. The first and last characters are the same
    # 2. All the characters in the middle (that smaller string) must be
    #     a palindrome.

    if len(the_string) <= 1:
        return True

    if the_string[0] != the_string[-1]:
        return False

    if not is_palindrome(the_string[1:-1]):
        return False

    return True


def main() -> None:
    # A palindrome is a string that's the same forward and backward.

    print(is_palindrome('racecar'))
    print(is_palindrome('mom'))
    print(is_palindrome('dad'))
    print(is_palindrome(''))
    print(is_palindrome('J'))
    print(is_palindrome('hello'))

if __name__ == '__main__':
    main()
