from enum import Enum

import stringcase
from faker import Faker
from faker_extensions.abstract_providers import CategoryWeightedProvider
from faker_extensions.common_categories import Gender, BaseEnum


class MaritalStatus(BaseEnum):
    SINGLE = 'SING'
    MARRIED = 'MAR'
    CIVIL_PARTNERED = 'CIV'
    DIVORCED = 'DIV'
    WIDOWED = 'WID'

    def name_value(self):
        return self.name.lower().replace('_', ' ')


class MaritalStatusProvider(CategoryWeightedProvider):

    """Marital status distribution in the uk"""
    maritalStatus_distributions = {
        Gender.FEMALE: {
            MaritalStatus.SINGLE: 0.443277931,
            MaritalStatus.MARRIED: 0.406950707,
            MaritalStatus.CIVIL_PARTNERED: 0.001355847,
            MaritalStatus.DIVORCED: 0.077191377,
            MaritalStatus.WIDOWED: 0.071224138
        },
        Gender.MALE: {
            MaritalStatus.SINGLE: 0.507236172,
            MaritalStatus.MARRIED: 0.412576042,
            MaritalStatus.CIVIL_PARTNERED: 0.001631708,
            MaritalStatus.DIVORCED: 0.051325646,
            MaritalStatus.WIDOWED: 0.027230432
        }
    }

    def __init__(self, generator):
        super().__init__(self.maritalStatus_distributions, generator)

    def marital_status(self, gender):
        return self.get_choice(gender)


def main():
    fake = Faker(['en_UK'])
    fake.add_provider(MaritalStatusProvider(fake))
    status = fake.marital_status(Gender.MALE)
    print(Gender.MALE)
    print(status)
    print(status.name_value())
    status = fake.marital_status(Gender.FEMALE)
    print(Gender.FEMALE)
    print(status)
    print(status.name_value())


if __name__ == '__main__':
    main()
