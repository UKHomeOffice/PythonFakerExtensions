from enum import Enum
from faker import Faker
from faker_extensions.abstract_providers import WeightedProvider
from faker_extensions.common_categories import BaseEnum


class Faith(BaseEnum):
    CHRISTIAN = 1
    BUDDHIST = 2
    HINDU = 3
    JEWISH = 4
    MUSLIM = 5
    SIKH = 6
    OTHER = 7
    NONE = 8
    NOT_STATED = 9


class FaithProvider(WeightedProvider):
    """ Faith distribution in the uk """
    faith_distributions = {
        Faith.CHRISTIAN: 0.467,
        Faith.BUDDHIST: 0.005,
        Faith.HINDU: 0.018,
        Faith.JEWISH: 0.005,
        Faith.MUSLIM: 0.057,
        Faith.SIKH: 0.007,
        Faith.OTHER: 0.017,
        Faith.NONE: 0.421
    }

    def __init__(self, generator):
        super().__init__(self.faith_distributions, generator)

    def faith(self):
        return self.get_choice()


def main():
    fake = Faker(['en_UK'])
    fake.add_provider(FaithProvider(fake))

    faith = fake.faith()
    print(faith)
    print(faith.name.title())


if __name__ == '__main__':
    main()
