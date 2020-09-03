from faker import Faker
from faker_extensions.abstract_providers import CategoricalNormalProvider
from faker_extensions.common_categories import Gender


class HeightProvider(CategoricalNormalProvider):
    """ Provide Fake height based on someones gender"""

    height_distributions = {
        Gender.MALE: (178, 10),
        Gender.FEMALE: (163, 9)
    }

    def __init__(self, generator):
        super().__init__(self.height_distributions, generator)

    def height(self, gender):
        """ Get a height based on someones gender """
        return int(super().get_choice(gender))


def main():
    # How to create your own provider
    # Note you cannot have multiple locales!!!!
    fake = Faker(['en_UK'])
    # Add your provider
    fake.add_provider(HeightProvider(fake))
    # Use it!
    print(fake.height(Gender.MALE))
    print(fake.height(Gender.FEMALE))


if __name__ == '__main__':
    main()
