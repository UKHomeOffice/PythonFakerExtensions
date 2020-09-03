from enum import Enum
from faker import Faker
from faker_extensions.abstract_providers import WeightedProvider
from faker_extensions.common_categories import BaseEnum


class EyeColour(BaseEnum):
    BLUE = 1
    BROWN = 2
    GREEN = 3


class EyeColourProvider(WeightedProvider):
    """ Provide Fake eye colour. Example of categorical with weightings"""

    """ The most common eye colours and their distribution in the uk"""
    eye_colours = {
        EyeColour.BLUE: 0.48,
        EyeColour.GREEN: 0.3,
        EyeColour.BROWN: 0.22
    }

    def __init__(self, generator):
        super().__init__(self.eye_colours, generator)

    def eye_colour(self):
        return self.get_choice()


def main():
    # How to create your own provider
    # Note you cannot have multiple locales!!!!
    fake = Faker(['en_UK'])
    # Add your provider - note the construction of a non instance
    fake.add_provider(EyeColourProvider(fake))
    # Use it!
    colour = fake.eye_colour()
    print(colour)
    print(colour.name.title())


if __name__ == '__main__':
    main()
