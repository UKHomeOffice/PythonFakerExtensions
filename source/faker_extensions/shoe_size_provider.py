from faker import Faker
from faker_extensions.abstract_providers import CategoryWeightedProvider
from faker_extensions.common_categories import Gender


class ShoeSizeProvider(CategoryWeightedProvider):

    """ Shoe size distribution in the uk """
    shoe_size_distributions = {
        Gender.FEMALE: {
            3: 0.06,
            4: 0.125,
            5: 0.22,
            6: 0.25,
            7: 0.185,
            8: 0.1025,
            9: 0.05
        },
        Gender.MALE: {
            5: 0.01,
            5.5: 0.01,
            6: 0.02,
            6.5: 0.04,
            7: 0.07,
            7.5: 0.11,
            8: 0.13,
            8.5: 0.15,
            9: 0.14,
            9.5: 0.12,
            10: 0.09,
            10.5: 0.06,
            11: 0.03,
            11.5: 0.02,
            12: 0.01
        }
    }

    def __init__(self, generator):
        super().__init__(self.shoe_size_distributions, generator)

    def shoe_size(self, category):
        return self.get_choice(category)


def main():
    fake = Faker(['en_UK'])
    fake.add_provider(ShoeSizeProvider(fake))
    size = fake.shoe_size(Gender.MALE)
    print(Gender.MALE)
    print(size)
    size = fake.shoe_size(Gender.FEMALE)
    print(Gender.FEMALE)
    print(size)


if __name__ == '__main__':
    main()
