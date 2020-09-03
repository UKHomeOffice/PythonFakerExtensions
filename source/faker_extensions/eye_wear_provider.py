from faker import Faker

from faker_extensions.abstract_providers import CategoryWeightedProvider
from faker_extensions.common_categories import Gender, BaseEnum


class EyeWearStatus(BaseEnum):
    """ Categories of eye wear """
    GLASSES = 1
    CONTACTS = 2
    NONE = 3


class EyeWearProvider(CategoryWeightedProvider):
    """ Eye wear distribution in the uk """
    eyeWear_distributions = {
        Gender.FEMALE: {
            EyeWearStatus.GLASSES: 0.72,
            EyeWearStatus.CONTACTS: 0.16,
            EyeWearStatus.NONE: 0.12
        },
        Gender.MALE: {
            EyeWearStatus.GLASSES: 0.66,
            EyeWearStatus.CONTACTS: 0.11,
            EyeWearStatus.NONE: 0.23
        }
    }

    def __init__(self, generator):
        super().__init__(self.eyeWear_distributions, generator)

    def eye_wear(self, gender):
        return self.get_choice(gender)


def main():
    """ Get eye wear by gender and distribution """
    fake = Faker(['en_UK'])
    fake.add_provider(EyeWearProvider(fake))
    eye_wear = fake.eye_wear(Gender.MALE)
    print(Gender.MALE)
    print(eye_wear)
    print(eye_wear.name.title())
    eye_wear = fake.eye_wear(Gender.FEMALE)
    print(Gender.FEMALE)
    print(eye_wear)
    print(eye_wear.name.title())


if __name__ == '__main__':
    main()
