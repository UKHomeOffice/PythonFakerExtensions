from enum import Enum
from random import randint

from faker import Faker
from faker_extensions.abstract_providers import WeightedProvider
from faker_extensions.common_categories import Gender
from faker_extensions.distinguishing_features_provider import BodyArea


class TattooProvider(WeightedProvider):
    """ Eye wear distribution in the uk """
    tattoo_distributions = {
        Gender.FEMALE: 0.47,
        Gender.MALE: 0.33
    }

    def __init__(self, generator):
        super().__init__(self.tattoo_distributions, generator)

    def tattoo(self):
        """ Returns if a person has a tattoo and location """
        choice = self.get_choice()
        random_body_area = BodyArea(randint(1, len(BodyArea.__members__)))
        return {choice, random_body_area}


def main():
    """ Get tattoo's by gender and distribution """
    fake = Faker(['en_UK'])
    fake.add_provider(TattooProvider(fake))
    tattoo = fake.tattoo()
    print(tattoo)


if __name__ == '__main__':
    main()
