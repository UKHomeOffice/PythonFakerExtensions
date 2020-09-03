from enum import Enum
from faker import Faker
from faker_extensions.abstract_providers import WeightedProvider
from faker_extensions.common_categories import BaseEnum


class Handedness(BaseEnum):
    LEFT = 1
    RIGHT = 2
    AMBIDEXTROUS = 3


class HandednessProvider(WeightedProvider):
    """ Provide Fake handedness based on uk stats"""

    handedness_weights = {
        Handedness.LEFT: 0.10,
        Handedness.RIGHT: 0.89,
        Handedness.AMBIDEXTROUS: 0.01
    }

    def __init__(self, generator):
        super().__init__(self.handedness_weights, generator)

    def handedness(self):
        return self.get_choice()


def main():
    # How to create your own provider
    # Note you cannot have multiple locales!!!!
    fake = Faker(['en_UK'])
    # Add your provider - note the construction of a non instance
    fake.add_provider(HandednessProvider(fake))
    # Use it!
    handedness = fake.handedness()
    print(handedness)
    print(handedness.name.title())


if __name__ == '__main__':
    main()
