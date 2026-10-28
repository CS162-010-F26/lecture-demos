class City:
    name: str

def main() -> None:
    # Every piece of data in Python is an object.

    # Every object has an id. You can get the id of
    # an object by passing it to the id() function.

    #print(5)

    # At a given point in time in a Python program,
    # every object in existence is guaranteed to have
    # a UNIQUE id. The id of an object does not change.

    x = 5
    #print(id(5)) # This prints the same ID as below!
    #print(id(x)) # This prints the same ID as above!

    # x is NOT an object. x is NOT a piece of data.
    # x is a variable, which is a kind of reference.
    # a reference is something that refers to an object.

    # Anytime a variable is used in an expression, the interpreter
    # replaces the variable (reference) with the object
    # that it refers to at the time the expression is evaluated.

    # The assignment operator (=) takes a reference on the left,
    # and an object on the right, and it binds the reference
    # to the object. That is, it makes the reference refer to
    # the given object.

    # Primitives (int, float, bool, str, and maybe others) are
    # all immutable (they're constants; they cannot be changed).


    # Tells y to refer to 5
    y = x
    print(id(x))
    print(id(y))

    # This line of code does NOT change an int from 5 to 6.
    # It changes x, telling it to refer to a new object.
    # It tells x to refer to the object 6, INSTEAD of the object 5.
    print(id(x))
    x = 6
    print(id(x))

    # When I change x and tell it to refer to 6 instead of 5, the
    # interpreter has to create the object 6. This takes up new memory.
    # The object 6 is stored in some location in memory.
    # The object 5 is stored in a different location in memory.

    # You can think of it as if x "points" to the place in memory
    #    where the 6 is located, whereas y "points" to the place in
    #    memory where the 5 is located.

    # That is all to say, the = operator does not change objects.
    # It changes references, telling them to point to different
    # places (i.e., to refer to different objects).

    # On the other hand, the dot operator (.), and the subscript
    # operator ([]), operate on objects. They reach inside objects
    # to access references inside them.
    
    my_city = City()
    my_city.name = 'Corvallis'

    # my_city refers to a City object.
    # Inside that object is an attribute (reference) called "name"
    # that refers to a string object ('Corvallis')

    # This tells another_city to refer to the City object that was
    # created in the constructor call on line 66.
    another_city = my_city
    # Currently, another_city and my_city refer to the same City object,
    # so this reaches inside that single City object and changes
    # its name to Eugene
    another_city.name = 'Eugene'
    print(my_city.name) # Prints Eugene

    another_city = City()
    # Now, another_city and my_city refer to two DIFFERENT
    # city objects. So when we change another_city.name,
    # that does NOT change my_city.name.
    another_city.name = 'Portland'
    print(my_city.name) # Prints Eugene



if __name__ == '__main__':
    main()
