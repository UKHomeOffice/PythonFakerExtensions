from enum import Enum
from faker import Faker
from faker_extensions.abstract_providers import CategoryWeightedProvider
from faker_extensions.common_categories import Gender, BaseEnum


class HairColour(BaseEnum):
    RED = 1
    BLONDE = 2
    LIGHT_BROWN = 3
    DARK_BROWN = 4
    BLACK = 5
    OTHER = 6


class HairColourProvider(CategoryWeightedProvider):
    """ Provide Fake hair colour."""

    """ The most common hair colours and their distribution in the uk"""
    hair_colours = {
        Gender.MALE: {
            HairColour.RED: 0.038,
            HairColour.BLONDE: 0.1,
            HairColour.LIGHT_BROWN: 0.4,
            HairColour.DARK_BROWN: 0.372,
            HairColour.BLACK: 0.074,
            HairColour.OTHER: 0.02
        },
        Gender.FEMALE: {
            HairColour.RED: 0.052,
            HairColour.BLONDE: 0.127,
            HairColour.LIGHT_BROWN: 0.425,
            HairColour.DARK_BROWN: 0.372,
            HairColour.BLACK: 0.015,
            HairColour.OTHER: 0.009
        }
    }

    def __init__(self, generator):
        super().__init__(self.hair_colours, generator)

    def hair_colour(self, gender):
        return self.get_choice(gender)


def main():
    # How to create your own provider
    # Note you cannot have multiple locales!!!!
    fake = Faker(['en_UK'])
    # Add your provider - note the construction of a non instance
    fake.add_provider(HairColourProvider(fake))
    # Use it!
    colour = fake.hair_colour(Gender.MALE)
    print(colour)
    print(colour.name.title())
    colour = fake.hair_colour(Gender.FEMALE)
    print(colour)
    print(colour.name.title())


if __name__ == '__main__':
    main()
