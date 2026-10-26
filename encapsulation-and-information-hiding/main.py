# Maintainability: A measure of how easy it is to maintain a codebase.

# Encapsulation is a tool (technique) that can help improve maintainability
# in a couple ways:
# 1. It can help control coupling
# 2. It can help establish class invariants

# Coupling: Problem that occurs such that changing one line of code
# requires changing one or more other lines of code.

# Encapsulation: Bundling (or co-locating) data (fields) with the
#   behaviors (functions) that operate on that data.

# For code to be well-encapsulated, it's not enough to just have the
# data and behavior together. You also need them to be isolated from other,
# unrelated data / behaviors.

# There is a concept known as Cohesion, which is a loose measure of how
# closely related your code components are to one another, given how
# close they are to one another.

# Encapsulation can help control coupling. First, I should point out
# that coupling is, to some extent, inevitable. Coupling occurs at interfaces,
# which are used in every dependency.

# However, coupling can make things hard to change. But consider:
# That's only an issue if the thing that's hard to change NEEDS to be
# changed.

# Dependency: 

def foo() -> str:
    print('Hello')
    return '5'

def main() -> None:
    # The main function depends on the foo() function.
    # The main function is a dependent.
    # The foo function is the dependency.
    # Specifically, the main function depends on the interface of the
    # foo function. The interface of a code component is the part of the
    # code component that other components directly interact with.
    print(int(foo()) * 3.5)

if __name__ == '__main__':
    main()
