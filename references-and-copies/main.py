from copy import deepcopy, copy

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
    #print(id(x))
    #print(id(y))

    # This line of code does NOT change an int from 5 to 6.
    # It changes x, telling it to refer to a new object.
    # It tells x to refer to the object 6, INSTEAD of the object 5.
    #print(id(x))
    x = 6
    #print(id(x))

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
    # print(my_city.name) # Prints Eugene

    another_city = deepcopy(my_city)
    another_city.name = 'Corvallis' # This does NOT modify my_city.name
    print(another_city.name) # Prints Corvallis
    print(my_city.name) # Prints Eugene



    another_city = City()
    # Now, another_city and my_city refer to two DIFFERENT
    # city objects. So when we change another_city.name,
    # that does NOT change my_city.name.
    another_city.name = 'Portland'
    # print(my_city.name) # Prints Eugene

    
    # The copy() function creates a shallow copy of the given object.
    # The deepcopy() function creates a deep copy of the given object.

    # Suppose an object a contains an attribute b, which contains an
    # attribute c.

    # Suppose you copy a via z = copy(a). z now refers to a shallow copy of
    # a. What this means: z and a refer to two different objects. However,
    # z.b refers to the same object as a.b. This is a shallow copy.

    # A consequence is that z.b.c also refers to the same object as a.b.c.
    # If I modify a.b.c, that will also modify z.b.c.
    # a.b.c = 'hello', this will modify z.b.c to be 'hello'
    # However, If I modify a.b, that will NOT modify z.b.
    # a.b = SomeCoolObject(), that will not modify z.b.

    # A deep copy, on the other hand, is a "full", proper copy.
    # If I say z = deepcopy(a), this traverses the object graph contained
    # within a. It copies everything that it finds. z is a proper, deep copy
    # of a. z and a refer to two different objects, but so do z.b and a.b,
    # and so do z.b.c and a.b.c

    

    


    


if __name__ == '__main__':
    main()
