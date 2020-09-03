import random
from faker import Faker

import faker_extensions.data.occupations as occupations
from faker_extensions.abstract_providers import CategoryWeightedProvider
from faker_extensions.common_categories import Gender


class OccupationProvider(CategoryWeightedProvider):
    """ Provide Fake occupation based on real data"""

    def __init__(self, generator):
        super().__init__(occupations.occs, generator)

    def occupation(self, gender):
        return self.get_choice(gender)


def main():
    # How to create your own provider
    # Note you cannot have multiple locales!!!!
    fake = Faker(['en_UK'])
    # Add your provider - note the construction of a non instance
    fake.add_provider(OccupationProvider(fake))
    # Use it!
    occ = fake.occupation(Gender.MALE)
    print(occ)
    occ = fake.occupation(Gender.FEMALE)
    print(occ)


if __name__ == '__main__':
    main()
