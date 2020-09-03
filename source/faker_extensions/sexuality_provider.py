from enum import Enum
from faker import Faker
from faker_extensions.abstract_providers import CategoryWeightedProvider
from faker_extensions.common_categories import Gender, BaseEnum


class Sexuality(BaseEnum):
    HETEROSEXUAL_STRAIGHT = 1
    GAY_LESBIAN = 2
    BISEXUAL = 3
    OTHER = 4
    UNKNOWN = 5
    NOT_PROVIDED = 6


class SexualityProvider(CategoryWeightedProvider):

    """Sexuality distribution in the uk"""
    sexuality_distributions = {
        Gender.FEMALE: {
            Sexuality.HETEROSEXUAL_STRAIGHT: 0.931,
            Sexuality.GAY_LESBIAN: 0.007,
            Sexuality.BISEXUAL: 0.007,
            Sexuality.OTHER: 0.003,
            Sexuality.UNKNOWN: 0.04,
            Sexuality.NOT_PROVIDED: 0.013
        },
        Gender.MALE: {
            Sexuality.HETEROSEXUAL_STRAIGHT: 0.925,
            Sexuality.GAY_LESBIAN: 0.015,
            Sexuality.BISEXUAL: 0.003,
            Sexuality.OTHER: 0.003,
            Sexuality.UNKNOWN: 0.038,
            Sexuality.NOT_PROVIDED: 0.016
        }
    }

    def __init__(self, generator):
        super().__init__(self.sexuality_distributions, generator)

    def sexuality(self, gender):
        return self.get_choice(gender)


def main():
    fake = Faker(['en_UK'])
    fake.add_provider(SexualityProvider(fake))
    sexuality = fake.sexuality(Gender.MALE)
    print(sexuality)
    print(sexuality.name.title())
    sexuality = fake.sexuality(Gender.FEMALE)
    print(sexuality)
    print(sexuality.name.title())


if __name__ == '__main__':
    main()
