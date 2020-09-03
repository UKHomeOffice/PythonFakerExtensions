from enum import Enum

import stringcase
from faker import Faker

from faker_extensions.abstract_providers import WeightedProvider


# https://www.pfma.org.uk/pet-population-2017
class Pets(Enum):
    INDOOR_FISH = 1
    OUTDOOR_FISH = 2
    DOG = 3
    CAT = 4
    RABBIT = 5
    INDOOR_BIRD = 6
    REPTILE = 7
    DOMESTIC_FOWL = 7
    GUINEA_PIG = 8
    HAMSTER = 9

    def name_value(self):
        return stringcase.sentencecase(self.name.lower())


pet_distributions = {
    Pets.INDOOR_FISH: 0.08,
    Pets.OUTDOOR_FISH: 0.05,
    Pets.DOG: 0.24,
    Pets.CAT: 0.17,
    Pets.RABBIT: 0.02,
    Pets.INDOOR_BIRD: 0.01,
    Pets.REPTILE: 0.02,
    Pets.DOMESTIC_FOWL: 0.01,
    Pets.GUINEA_PIG: 0.02,
    Pets.HAMSTER: 0.01,
    None: 0.37
}


class PetProvider(WeightedProvider):

    def __init__(self, generator):
        super().__init__(pet_distributions, generator)

    def pet(self):
        return self.get_choice()


def main():
    fake = Faker(['en_UK'])
    fake.add_provider(PetProvider(fake))

    pet = fake.pet()
    print(pet)


if __name__ == '__main__':
    main()
