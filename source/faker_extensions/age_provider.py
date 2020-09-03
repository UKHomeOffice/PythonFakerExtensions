from faker import Faker
from faker.providers.date_time import Provider

from faker_extensions.abstract_providers import BoundedWeightedProvider


class AgeProvider(BoundedWeightedProvider):
    """ Provide Fake age and date of birth"""

    age_distribution = {
        (0, 4): 0.062,
        (5, 9): 0.056,
        (10, 14): 0.058,
        (15, 17): 0.037,
        (18, 24): 0.094,
        (25, 29): 0.068,
        (30, 34): 0.066,
        (35, 39): 0.067,
        (40, 44): 0.073,
        (45, 49): 0.073,
        (50, 54): 0.064,
        (55, 59): 0.057,
        (60, 64): 0.06,
        (65, 69): 0.048,
        (70, 74): 0.039,
        (75, 79): 0.032,
        (80, 84): 0.024,
        (85, 100): 0.022
    }

    def __init__(self, generator):
        super().__init__(self.age_distribution, generator)
        self.date_provider = Provider(generator)

    def age(self):
        """ Get a random age and date of birth based on a maximum age of 100 from today """
        age_in_years = super().get_choice()
        return age_in_years, self.date_provider.date_between(
            start_date='-{}y'.format(age_in_years + 1),
            end_date='-{}y'.format(age_in_years)
        )


def main():
    # How to create your own provider
    # Note you cannot have multiple locales!!!!
    fake = Faker(['en_UK'])
    # Add your provider
    fake.add_provider(AgeProvider(fake))
    # Use it!
    print(fake.age())


if __name__ == '__main__':
    main()
