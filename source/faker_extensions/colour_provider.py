from enum import Enum
from random import randint
from faker import Faker
from faker.providers import BaseProvider

from faker_extensions.common_categories import BaseEnum


class Colour(BaseEnum):
    RED = 1
    YELLOW = 2
    BLUE = 3
    ORANGE = 4
    GREEN = 5
    VIOLET = 6


class ColourProvider(BaseProvider):
    """ Provide Fake (simple) colour. Example of categorical"""

    # noinspection PyMethodMayBeStatic
    def colour(self):
        return Colour(randint(1, len(Colour.__members__)))


def main():
    # How to create your own provider
    # Note you cannot have multiple locales!!!!
    fake = Faker(['en_UK'])
    # Add your provider
    fake.add_provider(ColourProvider)
    # Use it!
    colour = fake.colour()
    print(colour)
    print(colour.name.title())


if __name__ == '__main__':
    main()
