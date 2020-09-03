from faker import Faker
from faker.providers import BaseProvider

from faker_extensions.common_categories import Gender


class NameProvider(BaseProvider):
    """ Provide Fake name as a dictionary"""

    def fielded_name(self, gender):
        if gender is Gender.MALE:
            return {
                'title': self.generator.prefix_male(),
                'firstName': self.generator.first_name_male(),
                'lastName': self.generator.last_name_male(),
            }
        else:
            return {
                'title': self.generator.prefix_female(),
                'firstName': self.generator.first_name_female(),
                'lastName': self.generator.last_name_female(),
            }


def main():
    # How to create your own provider
    # Note you cannot have multiple locales!!!!
    fake = Faker(['en_US'])
    # Add your provider
    fake.add_provider(NameProvider)
    # Use it!
    print(fake.fielded_name(Gender.MALE))
    print(fake.fielded_name(Gender.FEMALE))


if __name__ == '__main__':
    main()
