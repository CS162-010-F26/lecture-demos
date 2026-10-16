# This is a Python module. Basically, any .py file is a Python module.

class Cat:
    color: str
    owner: str
    age: int

def create_cat(color: str, owner: str, age: int) -> Cat:
    result = Cat()
    result.color = color
    result.owner = owner
    result.age = age
    return result

def print_cat(the_cat: Cat) -> None:
    print(the_cat.color)
    print(the_cat.owner)
    print(the_cat.age)
