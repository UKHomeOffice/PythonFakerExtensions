from faker import Faker
from faker_extensions.common_categories import Gender
from faker_extensions.abstract_providers import WeightedProvider


class GenderProvider(WeightedProvider):

    """ Gender distribution in the uk"""
    gender_distributions = {
        Gender.MALE: 0.4917,
        Gender.FEMALE: 0.5083
    }

    def __init__(self, generator):
        super().__init__(self.gender_distributions, generator)

    def gender(self):
        return self.get_choice()


def main():
    fake = Faker(['en_UK'])
    fake.add_provider(GenderProvider(fake))

    gender = fake.gender()
    print(gender)
    print(gender.short_code)
    print(gender.name.title())


if __name__ == '__main__':
    main()
