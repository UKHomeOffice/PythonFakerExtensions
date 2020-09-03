from faker import Faker
from faker_extensions.abstract_providers import CategoricalNormalProvider
from faker_extensions.common_categories import Gender


class WeightProvider(CategoricalNormalProvider):
    """ Provide Fake height based on someones gender"""

    # data from 2011 https://academic.oup.com/jpubhealth/article/38/3/607/2239800
    bmi_distributions = {
        Gender.MALE: (27.5, 4.8),
        Gender.FEMALE: (27.2, 5.8)
    }

    def __init__(self, generator):
        super().__init__(self.bmi_distributions, generator)

    def weight(self, gender, height):
        """ Get a height based on someones gender """
        height_in_meters = height/100
        bmi = float(super().get_choice(gender))

        return round(bmi * height_in_meters * height_in_meters), bmi


def main():
    # How to create your own provider
    # Note you cannot have multiple locales!!!!
    fake = Faker(['en_UK'])
    # Add your provider
    fake.add_provider(WeightProvider(fake))
    # Use it!
    print(fake.weight(Gender.MALE, 178))
    print(fake.weight(Gender.FEMALE, 163))


if __name__ == '__main__':
    main()
