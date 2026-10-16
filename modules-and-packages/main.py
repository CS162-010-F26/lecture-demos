# import is used to import, or load, other packages or modules

# import can be used to import your own custom, local modules / packages.
# When you use the import keyword, it first checks to see if there
# is a local module / package with the given name in your import path.
# If no such module / package exists, it will then check the entire
# system to see if there's a system-installed package / module with
# that name.
import animals.dog as d
import animals.cat as c
# from animals import dog as d

# from animals.dog import create_dog, print_dog, Dog

def main() -> None:
    clifford = d.create_dog('Big Red', 'Johnson', 40)

    d.print_dog(clifford)

    garfield = c.create_cat('Orange', 'John', 30)

    c.print_cat(garfield)

if __name__ == '__main__':
    main()
