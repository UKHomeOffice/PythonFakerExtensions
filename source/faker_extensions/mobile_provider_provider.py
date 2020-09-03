from enum import Enum

import stringcase
from faker import Faker

from faker_extensions.abstract_providers import WeightedProvider


class MobileProviders(Enum):
    EE = 1
    O2 = 2
    VODAFONE = 3
    THREE = 4
    TESCO_MOBILE = 5
    VIRGIN_MOBILE = 6
    GIFFGAFF = 7

    def name_value(self):
        return stringcase.sentencecase(self.name.lower())


mobile_provider_distributions = {
    # use raw subscribers as weights
    # https://en.wikipedia.org/wiki/List_of_mobile_network_operators_of_Europe#United_Kingdom
    MobileProviders.EE: 28.9,
    MobileProviders.O2: 26.0,
    MobileProviders.VODAFONE: 18.1,
    MobileProviders.THREE: 13.3,
    # MVNOs https://www.grantthornton.co.uk/globalassets/1.-member-firms/united-kingdom/pdf/publication/state-of-the-uk-mvno-market.pdf
    MobileProviders.TESCO_MOBILE: 4.6,
    MobileProviders.VIRGIN_MOBILE: 3.0,
    MobileProviders.GIFFGAFF: 2.0
}


class MobileProviderProvider(WeightedProvider):

    def __init__(self, generator):
        super().__init__(mobile_provider_distributions, generator)

    def mobile_provider(self):
        return self.get_choice()


def main():
    fake = Faker(['en_UK'])
    fake.add_provider(MobileProviderProvider(fake))

    provider = fake.mobile_provider()
    print(provider.name_value())


if __name__ == '__main__':
    main()
