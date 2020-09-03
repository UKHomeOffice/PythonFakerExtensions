import random
from enum import Enum
from faker import Faker
from faker_extensions.abstract_providers import CategoryWeightedProvider
from faker_extensions.common_categories import Gender, BaseEnum


class DyedHairColour(BaseEnum):
    RED = 1
    BLONDE = 2
    BROWN = 3
    BLACK = 5
    OTHER = 6


class DyedHairColourProvider(CategoryWeightedProvider):
    """ Provide Fake dyed hair colour"""

    """ The most common hair colours and their distribution in the uk"""
    dyed_hair_colours = {
        Gender.MALE: {
            DyedHairColour.RED: 0.038,
            DyedHairColour.BLONDE: 0.1,
            DyedHairColour.BROWN: 0.372,
            DyedHairColour.BLACK: 0.074,
            DyedHairColour.OTHER: 0.02
        },
        Gender.FEMALE: {
            DyedHairColour.RED: 0.052,
            DyedHairColour.BLONDE: 0.127,
            DyedHairColour.BROWN: 0.372,
            DyedHairColour.BLACK: 0.015,
            DyedHairColour.OTHER: 0.009
        }
    }

    def __init__(self, generator):
        super().__init__(self.dyed_hair_colours, generator)

    def dyed_hair_colour(self, gender):
        """Build in the randomness"""
        if gender is Gender.FEMALE:
            if random.randrange(0, 100) < 85:
                return self.get_choice(gender)
            else:
                return None
        if gender is Gender.MALE:
            if random.randrange(0, 100) < 11:
                return self.get_choice(gender)
            else:
                return None
        raise ValueError("Unknown gender: {}".format(gender))


def main():
    # How to create your own provider
    # Note you cannot have multiple locales!!!!
    fake = Faker(['en_UK'])
    # Add your provider - note the construction of a non instance
    fake.add_provider(DyedHairColourProvider(fake))
    # Use it!
    colour = fake.dyed_hair_colour(Gender.MALE)
    print(colour)
    colour = fake.dyed_hair_colour(Gender.FEMALE)
    print(colour)


if __name__ == '__main__':
    main()
