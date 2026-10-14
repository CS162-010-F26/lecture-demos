# Create a very simple program that opens
# data.txt for reading,
# reads each line in a for loop,
# splits the line by commas (.split()
# method of the string class),
# creates a City object (you'll have
# to define the City class),
# and stores the name and population
# inside respective fields of the
# City object.

# Define your City class.
class City:
    name: str
    population: int

def main() -> None:
    cities = []
    with open('data.txt', 'r') as my_file:
        for line in my_file:
            # Use line.split(), create a
            # City(), store the values
            # in the fields.
            tokens = line.split(',')
            name = tokens[0]
            population = int(tokens[1])
            city = City()
            city.name = name
            city.population = population
            cities.append(city)

    print(cities[0].name)

if __name__ == '__main__':
    main()
