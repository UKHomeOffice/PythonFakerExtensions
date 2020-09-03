from enum import Enum
from faker import Faker
from faker_extensions.abstract_providers import WeightedProvider


class CarColour(Enum):
    SILVER_ALUMINIUM = 1
    BLACK = 2
    BLUE = 3
    GREY = 4
    WHITE = 5
    RED = 6
    GREEN = 7
    BEIGE_BUFF = 8
    BROWN = 9
    YELLOW = 10
    ORANGE = 11
    GOLD = 12
    PURPLE_MAUVE_VIOLET = 13
    BRONZE = 14
    TURQUOISE = 15
    MAROON = 16
    CREAM_IVORY = 17
    PINK = 18
    MULTICOLOURED = 19
    NOT_STATED = 20


class VehicleColourProvider(WeightedProvider):
    """ Provide Fake vehicle colour. Example of categorical with weightings"""

    """ The most common car colours and their distribution in the uk"""
    # https://www.gizmodo.co.uk/2018/07/government-statistics-reveal-the-most-common-car-colours-on-britains-roads/
    # todo: find the original source of this from the DVLA
    car_colours = {
        CarColour.SILVER_ALUMINIUM: 20.3,
        CarColour.BLACK: 19.93,
        CarColour.BLUE: 17.83,
        CarColour.GREY: 13.45,
        CarColour.WHITE: 11.39,
        CarColour.RED: 10.64,
        CarColour.GREEN: 2.69,
        CarColour.BEIGE_BUFF: 0.71,
        CarColour.BROWN: 0.59,
        CarColour.YELLOW: 0.54,
        CarColour.ORANGE: 0.53,
        CarColour.GOLD: 0.40,
        CarColour.PURPLE_MAUVE_VIOLET: 0.37,
        CarColour.BRONZE: 0.25,
        CarColour.TURQUOISE: 0.11,
        CarColour.MAROON: 0.10,
        CarColour.CREAM_IVORY: 0.08,
        CarColour.PINK: 0.06,
        CarColour.MULTICOLOURED: 0.02,
        CarColour.NOT_STATED: 0.0,
    }

    def __init__(self, generator):
        super().__init__(self.car_colours, generator)

    def vehicle_colour(self):
        return self.get_choice()


def main():
    # How to create your own provider
    # Note you cannot have multiple locales!!!!
    fake = Faker(['en_UK'])
    # Add your provider - note the construction of a non instance
    fake.add_provider(VehicleColourProvider(fake))
    # Use it!
    colour = fake.vehicle_colour()
    print(colour)
    print(colour.name.title())


if __name__ == '__main__':
    main()
