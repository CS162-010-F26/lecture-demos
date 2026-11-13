from vendor import Vendor

from furniture import Furniture
from car import Car

def main() -> None:
    jacob = Vendor[Furniture]()
    couch = Furniture()
    couch.name = 'Couch'
    couch.price = 300.00
    chair = Furniture()
    chair.name = 'Chair'
    chair.price = 25.00
    jacob.add_item_to_stock(couch)
    jacob.add_item_to_stock(chair)

    jacob.print()

    jacob.sell_item(0)

    jacob.print()

    samantha = Vendor[Car]()
    ford_taurus = Car()
    ford_taurus.make = 'Ford'
    ford_taurus.model = 'Taurus'
    ford_taurus.year = 2001
    ford_taurus.price = 800.00

    jeep_grand_cherokee = Car()
    jeep_grand_cherokee.make = 'Jeep'
    jeep_grand_cherokee.model = 'Grand Cherokee'
    jeep_grand_cherokee.year = 2009
    jeep_grand_cherokee.price = 3000.00
    samantha.add_item_to_stock(ford_taurus)
    samantha.add_item_to_stock(jeep_grand_cherokee)

    rocking_chair = Furniture()
    rocking_chair.name = 'Rocking Chair'
    rocking_chair.price = 100.00

    # This now yields an error, because rocking_chair is of type
    # Furniture, but T (in the context of samantha) is the typename
    # Car. A Furniture object is not a Car.
    # samantha.add_item_to_stock(rocking_chair)

    samantha.print()

    samantha.sell_item(0)

    samantha.print()

if __name__ == '__main__':
    main()
