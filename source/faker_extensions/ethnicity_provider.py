from enum import Enum

from faker import Faker

from faker_extensions.abstract_providers import WeightedProvider


class Ethnicity(Enum):

    def __init__(self, value, skin_colour):
        self._value_ = value
        self.skin_colour = skin_colour

    WHITE = (1, 'White')
    MIXED_MULTIPLE_ETHNIC_GROUPS = (2, 'Brown')
    ASIAN_ASIAN_BRITISH = (3, 'Brown')
    BLACK_AFRICAN_CARIBBEAN_BLACK_BRITISH = (4, 'Black')
    CHINESE = (5, 'Yellow')
    ARAB = (6, 'Olive')
    OTHER = (7, 'Unknown')


class EthnicityCodes(Enum):
    A1 = ("Indian", Ethnicity.ASIAN_ASIAN_BRITISH)
    A2 = ("Pakistani", Ethnicity.ASIAN_ASIAN_BRITISH)
    A3 = ("Bangladeshi", Ethnicity.ASIAN_ASIAN_BRITISH)
    A9 = ("Any other Asian background", Ethnicity.ASIAN_ASIAN_BRITISH)
    B1 = ("Caribbean", Ethnicity.BLACK_AFRICAN_CARIBBEAN_BLACK_BRITISH)
    B2 = ("African", Ethnicity.BLACK_AFRICAN_CARIBBEAN_BLACK_BRITISH)
    B9 = ("Any other Black background", Ethnicity.BLACK_AFRICAN_CARIBBEAN_BLACK_BRITISH)
    M1 = ("White and Black Caribbean", Ethnicity.MIXED_MULTIPLE_ETHNIC_GROUPS)
    M2 = ("White and Black African", Ethnicity.MIXED_MULTIPLE_ETHNIC_GROUPS)
    M3 = ("White and Asian", Ethnicity.MIXED_MULTIPLE_ETHNIC_GROUPS)
    M9 = ("Any other mixed background", Ethnicity.MIXED_MULTIPLE_ETHNIC_GROUPS)
    O1 = ("Chinese", Ethnicity.CHINESE)
    O9 = ("Any other ethnic group", Ethnicity.OTHER)
    W1 = ("White British", Ethnicity.WHITE)
    W2 = ("White Irish", Ethnicity.WHITE)
    W9 = ("Any other White background", Ethnicity.WHITE)


class EthnicityProvider(WeightedProvider):
    # https://www.ethnicity-facts-figures.service.gov.uk/uk-population-by-ethnicity/national-and-regional-populations/population-of-england-and-wales/latest
    """ Ethnicity distribution in the uk"""
    ethnicity_distributions = {
        EthnicityCodes.A1: 0.025,
        EthnicityCodes.A2: 0.02,
        EthnicityCodes.A3: 0.008,
        EthnicityCodes.A9: 0.015,
        EthnicityCodes.B1: 0.011,
        EthnicityCodes.B2: 0.018,
        EthnicityCodes.B9: 0.005,
        EthnicityCodes.M1: 0.008,
        EthnicityCodes.M2: 0.003,
        EthnicityCodes.M3: 0.006,
        EthnicityCodes.M9: 0.005,
        EthnicityCodes.O1: 0.007,
        EthnicityCodes.O9: 0.01,
        EthnicityCodes.W1: 0.805,
        EthnicityCodes.W2: 0.009,
        EthnicityCodes.W9: 0.045  # Combined "White Gypsy/Traveller" and "White other"
    }

    def __init__(self, generator):
        super().__init__(self.ethnicity_distributions, generator)

    def ethnicity(self):
        ethnicity = self.get_choice()
        return {
            'ethnicCode': ethnicity.name,
            'description': ethnicity.value[0],
            'skinColour': ethnicity.value[1].skin_colour
        }


def main():
    fake = Faker(['en_UK'])
    fake.add_provider(EthnicityProvider(fake))
    ethnicity = fake.ethnicity()
    print(ethnicity)
    print(ethnicity['description'])
    print(ethnicity['skinColour'])


if __name__ == '__main__':
    main()
